#coding=UTF-8

import pymysql

def getuserinfo(name):
    info = None;
    try:
        conn = pymysql.connect(host='localhost', user='root', passwd='sm%198809', db='test', port=3306);
        cur=conn.cursor();
        
        c = 'select * from urls where name = "%s"' % (name);
        print(c);
        cur.execute(c);
        info = cur.fetchall();
        print("first:")        
        print(info);

        cur.close();
        conn.close();
    except Exception:
        print("database exception...");
    
    return info;

'''
a = getuserinfo("tom");
b = str(type(a));
print(type(a));
print(a);
'''


