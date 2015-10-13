'''
    this file is to provide the interface between the url queue and mysql
    1.put a new url in the queue end
     when it has 1024 urls, befor insert a new one ,commit 512 urls to mysql database in table urls
    2.get a url form the queue
     if then queue is empty, read 512 urls from the database
'''

import pymysql
import bloomfilter

url_table_name = "urls";
url_queue = [];
bfcontain = bloomfilter.Bloom_Filter();
contain_size = 1024;

def create_urltable(cursor):
    '''when a table is not exist, create it
       when it exist, do none
    '''

    cursor.execute("show tables");
    tables = cursor.fetchall();

    ut_exist = False;
    for element in tables:
        if element[0] == url_table_name:
            ut_exist = True;

    if False == ut_exist:
        print("create urls table...")
        cursor.execute("create table %s(id int(16) not null auto_increment, url char(128) not null, PRIMARY KEY(id))" % url_table_name);
        print("create urls table success...")
        return 0;
    else:
        cursor.execute("select MAX(id) from %s" % url_table_name);
        maxid = cursor.fetchone();
        if maxid[0] is None:
            return 0;
        else:
            return maxid[0];


def insert_into_database(urls):
    ''' urls is a url list
    '''
    try:
        conn = pymysql.connect(host='localhost',user='root',passwd='sm%198809',db='test',port=3306)
        cur = conn.cursor();

        # create if not exist
        maxid = create_urltable(cur);

        url_templet = "insert %s values(%d, '%s')";
        for element in urls:
            maxid = maxid + 1;
            url = url_templet % (url_table_name, maxid, element);
            cur.execute(url);

        conn.commit()
        cur.close()
        conn.close()

    except Exception:
        print("exception...");


def insert_url_intoqueue(url):
    if not bfcontain.exists(url):
        bfcontain.mark_value(url);

        if len(url_queue) < contain_size :
            url_queue.append(url);
        else:
            urls_insert = [];
            i = 0;
            while i < contain_size / 2:
                urls_insert.append(url_queue.pop());
                i = i + 1;

            insert_into_database(urls_insert);

        return 0;
    print("++++++++" + str(url));


def getmixid(cursor):
    cursor.execute("select MIN(id) from %s" % url_table_name);
    minid = cursor.fetchone();
    if minid is None:
        return 0;
    else:
        return minid[0];

def get_url_formdatabase():
    '''get contain_size / 2 urls form database
    '''
    global url_queue;
    try:
        conn = pymysql.connect(host='localhost',user='root',passwd='sm%198809',db='test',port=3306)
        cur = conn.cursor();

        minid = getmixid(cur);
        minid = int(minid + contain_size/2);

        cur.execute("select url from %s where id < %d" % (url_table_name, minid));
        url_queue = list(cur.fetchall());
        #cur.execute("delete url from %s where id < %d" % url_table_name, minid);
        conn.commit()
        cur.close()
        conn.close()
    except Exception:
        print("exception...");


def get_url_fromqueue():
    '''get a url from the queue
    '''

    if len(url_queue) < 1 :
        get_url_formdatabase();

    print(url_queue);
    return url_queue.pop(0);

def url_print():
    for element in url_queue:
        print(element);

