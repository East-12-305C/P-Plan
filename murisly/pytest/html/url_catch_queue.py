#coding=UTF-8

'''
    this file is to provide the interface between the url queue and mysql
    1.put a new url in the queue end
     when it has 1024 urls, befor insert a new one ,commit 512 urls to mysql database in table urls
    2.get a url form the queue
     if then queue is empty, read 512 urls from the database
'''

import pymysql
import bloomfilter
import time


class UrlQueue():
    def __init__(self, tablename = "firstuser", queueasize = 8, count = 1 << 26):

        self.url_first = tablename;      #"firstuser"
        self.url_alluser = "alluser";    #"alluser"
        self.url_unvisituser = "unvisituser";    #"unvisituser"

        self.contain_size = queueasize;  #缓存队列的最大长度
        self.url_queue = [];             #缓存队列

        self.connect = None;
        self.create_urltable();

        self.bloomfilter = bloomfilter.Bloom_Filter(count);
        self.putdataurl_in_bloomfilter();


    def create_urltable(self, cursor):
        '''when a table is not exist, create it
           when it exist, do none
        '''

        cursor.execute("show tables");
        tables = cursor.fetchall();

        ut_firstuser = False;
        ut_alluser = False;
        for element in tables:
            if element[0] == self.url_firstuser:
                ut_firstuser = True;
            elif element[0] == self.url_alluser:
                ut_alluser = True;

        if False == ut_firstuser:
            print("create firstuser table...")
            cursor.execute("create table %s(id int(10) not null auto_increment, url char(32) not null, exist tinyint(2), PRIMARY KEY(id))" % self.url_firstuser);
            print("create firstuser table success...")
            return 0;

        if False == ut_alluser:
            print("create alluser table...")
            cursor.execute("create table %s(id int(10) not null auto_increment, url char(32) not null, PRIMARY KEY(id))" % self.url_alluser);
            print("create alluser table success...")
            return 0;

        # else:
        #     cursor.execute("select MAX(id) from %s" % self.url_firstuser);
        #     maxid = cursor.fetchone();
        #     if maxid[0] is None:
        #         return 0;
        #     else:
        #         return maxid[0];


    def putdataurl_in_bloomfilter(self):
        try:
            conn = pymysql.connect(host='localhost',user='root',passwd='east',db='test',port=3306)
            cur = conn.cursor();
            cur.execute("select * from %s" % self.url_firstuser);

            urls = cur.fetchall();
            for element in urls:
                self.bloomfilter.mark_value(element[1]);

            cur.close()
            conn.close()

        except Exception:
            nowtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()));
            print("UrlQueue exception time: " + nowtime);


        return 0;

    def getmixid(self, cursor):
        cursor.execute("select MIN(id) from %s where exist = 0" % self.url_firstuser);
        minid = cursor.fetchone();
        if minid is None:
            return 0;
        else:
            return minid[0];


    def insert_into_database(self, urls):
        ''' urls is a url list
        '''
        try:
            conn = pymysql.connect(host='localhost',user='root',passwd='east',db='test',port=3306)
            cur = conn.cursor();

            # create if not exist
            maxid = self.create_urltable(cur);

            url_templet = "insert %s values(%d, '%s', 0)";
            for element in urls:
                maxid = maxid + 1;
                url = url_templet % (self.url_firstuser, maxid, element);
                cur.execute(url);

            conn.commit()
            cur.close()
            conn.close()

        except Exception:
            nowtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()));
            print("insert_into_database exception time: " + nowtime);


    def get_url_formdatabase(self):
        '''get contain_size / 2 urls form database
        '''
        try:
            conn = pymysql.connect(host='localhost',user='root',passwd='east',db='test',port=3306)
            cur = conn.cursor();

            minid = self.getmixid(cur);
            if minid is not None:
                mixid = int(minid + self.contain_size/2);

                cur.execute("select url from %s where id between %d and %d" % (self.url_firstuser, minid, mixid));
                self.url_queue = list(cur.fetchall());
                cur.execute("update %s set exist = 1 where id between %d and %d" % (self.url_firstuser, minid, mixid));
                conn.commit();

            cur.close()
            conn.close()
        except Exception:
            nowtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()));
            print("get_url_formdatabase exception time: " + nowtime);


    def inserturl(self, url):
        if not self.bloomfilter.exists(url):
            self.bloomfilter.mark_value(url);

            self.url_queue.append(url);
            if len(self.url_queue) > self.contain_size :
                urls_insert = [];
                i = 0;
                while i < self.contain_size / 2:
                    urls_insert.append(self.url_queue.pop());
                    i = i + 1;

                self.insert_into_database(urls_insert);

            return 0;
        print("++++++++" + str(url));


    def geturl(self):
        if len(self.url_queue) < 1 :
            self.get_url_formdatabase();

        if len(self.url_queue) > 0 :
            return self.url_queue.pop(0);
        else :
            return None;



