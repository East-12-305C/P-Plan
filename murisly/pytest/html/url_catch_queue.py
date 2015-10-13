'''
    this file is to provide the interface between the url queue and mysql
    1.put a new url in the queue end
     when it has 1024 urls, befor insert a new one ,commit 512 urls to mysql database in table urls
    2.get a url form the queue
     if then queue is empty, read 512 urls from the database
'''

import pymysql
import bloomfilter


class UrlQueue():
    def __init__(self, tablename = "urls", queueasize = 4, count = 1 << 26):
        self.bloomfilter = bloomfilter.Bloom_Filter(count);
        self.url_table_name = tablename;
        self.contain_size = queueasize;
        self.url_queue = [];


    def getmixid(self, cursor):
        cursor.execute("select MIN(id) from %s" % self.url_table_name);
        minid = cursor.fetchone();
        if minid is None:
            return 0;
        else:
            return minid[0];


    def create_urltable(self, cursor):
        '''when a table is not exist, create it
           when it exist, do none
        '''

        cursor.execute("show tables");
        tables = cursor.fetchall();

        ut_exist = False;
        for element in tables:
            if element[0] == self.url_table_name:
                ut_exist = True;

        if False == ut_exist:
            print("create urls table...")
            cursor.execute("create table %s(id int(16) not null auto_increment, url char(128) not null, PRIMARY KEY(id))" % self.url_table_name);
            print("create urls table success...")
            return 0;
        else:
            cursor.execute("select MAX(id) from %s" % self.url_table_name);
            maxid = cursor.fetchone();
            if maxid[0] is None:
                return 0;
            else:
                return maxid[0];


    def insert_into_database(self, urls):
        ''' urls is a url list
        '''
        try:
            conn = pymysql.connect(host='localhost',user='root',passwd='sm%198809',db='test',port=3306)
            cur = conn.cursor();

            # create if not exist
            maxid = self.create_urltable(cur);

            url_templet = "insert %s values(%d, '%s')";
            for element in urls:
                maxid = maxid + 1;
                url = url_templet % (self.url_table_name, maxid, element);
                cur.execute(url);

            conn.commit()
            cur.close()
            conn.close()

        except Exception:
            print("insert exception...");


    def get_url_formdatabase(self):
        '''get contain_size / 2 urls form database
        '''
        try:
            conn = pymysql.connect(host='localhost',user='root',passwd='sm%198809',db='test',port=3306)
            cur = conn.cursor();

            minid = self.getmixid(cur);
            if minid is not None:
                minid = int(minid + self.contain_size/2);

                cur.execute("select url from %s where id < %d" % (self.url_table_name, minid));
                self.url_queue = list(cur.fetchall());
                cur.execute("delete from %s where id < %d" % (self.url_table_name, minid));
                conn.commit();

            cur.close()
            conn.close()
        except Exception:
            print("get exception...");


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


