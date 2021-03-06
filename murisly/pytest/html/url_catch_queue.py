#coding=UTF-8

'''
    this file is to provide the interface between the url queue and mysql
    1.put a new url in the queue end
     when it has 1024 urls, befor insert a new one ,commit 512 urls to mysql database in table urls
    2.get a url form the queue
     if then queue is empty, read 512 urls from the database
'''

import errormode
import pymysql
import bloomfilter


class sqlOperate():
    def __init__(self):
        self.connect = None
        self.cursor =None

        self.url_alluser     = "alluser"
        self.url_firstuser   = "firstuser"
        self.url_unvisituser = "unvisituser"

        try:
            self.connect = pymysql.connect(host='localhost',user='root',passwd='east',db='spider',port=3306, charset="gbk")
            self.cursor = self.connect.cursor()

            self.cursor.execute("show tables;")
            tables = self.cursor.fetchall()

            ut_firstuser = False
            ut_alluser = False
            ut_unvisituser = False
            for element in tables:
                if element[0] == self.url_firstuser:
                    ut_firstuser = True
                elif element[0] == self.url_alluser:
                    ut_alluser = True
                elif element[0] == self.url_unvisituser:
                    ut_unvisituser = True

            if False == ut_firstuser:
                print("create firstuser table...")
                self.cursor.execute("create table %s(id bigint(10) not null auto_increment, nickname char(32), sex tinyint(2), address char(10), birthday int(8), weibos int(6), follow int(9), interes int(5), PRIMARY KEY(id))" % self.url_firstuser);
                self.cursor.execute("alter table %s convert to charset gbk;" % (self.url_firstuser));
                print("create firstuser table success...")

            if False == ut_alluser:
                print("create alluser table...")
                self.cursor.execute("create table %s(id bigint(10) not null auto_increment, nickname char(32) not null, PRIMARY KEY(id))" % self.url_alluser);
                self.cursor.execute("alter table %s convert to charset gbk;" % (self.url_alluser));
                print("create alluser table success...")

            if False == ut_unvisituser:
                print("create unvisituser table...")
                self.cursor.execute("create table %s(id bigint(10) not null auto_increment, nums int, PRIMARY KEY(id))" % self.url_unvisituser);
                self.cursor.execute("alter table %s convert to charset gbk;" % (self.url_unvisituser));
                print("create unvisituser table success...")
        except Exception:
            errormode.errorWriting(__file__ + "  sqlOperate")


    def __del__(self):
        self.cursor.close()
        self.connect.close()


    def getUnvisit(self, inum):
        '''
        从数据表中取出未访问的num个用户, 病从数据表中删除
        :param num: 取出未访问的用户个数
        :return: 返回未访问用户的表
        '''
        userids = []
        try:
            self.cursor.execute("select * from %s limit %d;" % (self.url_unvisituser, inum));
            ret = self.cursor.fetchall()
            if len(ret) > 0 :
                userids = ret[0]
            self.cursor.execute("delete from %s limit %d;" % (self.url_unvisituser, inum));
            self.connect.commit();
        except Exception:
            errormode.errorWriting(__file__ + "  getUnvisit")

        return userids;


    def insertUnvisit(self, unList):
        '''
        将未访问的用户列表放到数据库中
        :param unList: 为访问的数据库列表
        :return:
        '''

        try:
            for element in unList:
                #print("insert %s valuse(%s);" % (self.url_unvisituser, element));
                self.cursor.execute("insert %s values(%s, 0) ON DUPLICATE KEY UPDATE nums=nums+1;" % (self.url_unvisituser, element));

            self.connect.commit();

        except Exception:
            errormode.errorWriting(__file__ + "  insertUnvisit");

    def getAlluser(self):
        allids = [];
        try:
            self.cursor.execute("select id from %s;" % (self.url_alluser));
            ret = self.cursor.fetchall();
            if len(ret) > 0 :
                for element in ret:
                    allids.append(element[0]);
        except Exception:
            errormode.errorWriting(__file__ + "  getAlluser");

        return allids;

    def updateAlluser(self, userid, nickname):
        try:
            sql = "insert alluser values(%d, '%s') ON DUPLICATE KEY UPDATE nickname = '%s';" % (int(userid), nickname, nickname)
            print(sql)
            self.cursor.execute(sql);
            self.connect.commit();
        except Exception:
            errormode.errorWriting(__file__ + "  updateAlluser");

    def updateFirstuser(self, userinfo):
        try:
            id = userinfo["id"];
            nickname = userinfo["nickname"];
            sex = userinfo["sex"];
            address = userinfo["address"];
            birthday = userinfo["birthday"];
            weibos = userinfo["weibos"];
            follow = userinfo["follow"];
            interes = userinfo["interes"];
            sql = 'insert firstuser values(%s,"%s",%s,"%s",%s,%s,%s,%s) ON DUPLICATE KEY UPDATE nickname="%s",sex=%s,address="%s",birthday=%s,weibos=%s,follow=%s,interes=%s;' % (id,nickname,sex,address,birthday,weibos,follow,interes, nickname,sex,address,birthday,weibos,follow,interes);
            print(sql);
            self.cursor.execute(sql);
            self.connect.commit();
        except Exception:
            errormode.errorWriting(__file__ + "  updateFirstuser");



class UrlQueue():
    '''
    缓存队列
    '''
    def __init__(self, tablename = "firstuser", queueasize = 1024, count = 1 << 26):
        self.sqlExec = sqlOperate();

        self.contain_size = queueasize;  #缓存队列的最大长度
        self.url_queue = [];             #缓存队列

        self.bloomfilter = bloomfilter.Bloom_Filter(count);
        self.putdataurl_in_bloomfilter();


    def putdataurl_in_bloomfilter(self):

        alluser = self.sqlExec.getAlluser();
        if alluser is not None:
            for element in alluser:
                self.bloomfilter.mark_value(element);

        return 0;


    def inserturl(self, url, nocheck = False):
        if nocheck :
            self.sqlExec.insertUnvisit(url);
            return ;

        if not self.bloomfilter.exists(url):
            #self.bloomfilter.mark_value(url);

            self.url_queue.append(url);
            if len(self.url_queue) > self.contain_size :
                urls_insert = [];
                i = 0;
                while i < self.contain_size / 2:
                    urls_insert.append(self.url_queue.pop());
                    i = i + 1;

                self.sqlExec.insertUnvisit(urls_insert);

            return 0;
        print("already exist user :" + str(url));


    def geturl(self):
        if len(self.url_queue) < 1 :
            self.url_queue = list(self.sqlExec.getUnvisit(int(self.contain_size / 2)));
        if len(self.url_queue) > 0 :
            return self.url_queue.pop(0);
        else :
            return None;


    def stop(self):
        '''
        停止时，把未访问的缓存队列中的内容放到数据库中
        :return:
        '''
        self.inserturl(self.url_queue, True);


    def updateAlluser(self, userinfo):
        self.sqlExec.updateAlluser(userinfo["id"], userinfo["nickname"]);

    def updateFirstuser(self, userinfo):
        self.sqlExec.updateFirstuser(userinfo);
