#coding=UTF-8

import pymysql
import collections

def getweibototal():
    result = collections.OrderedDict();
    try:
        conn = pymysql.connect(host='localhost', user='root', passwd='east', db='spider', port=3306, charset="utf8");
        cur = conn.cursor();
        
        sql = 'select nickname,follow from firstuser order by follow desc limit 10;'
        cur.execute(sql);
        ret = cur.fetchall();
        for element in ret:
            result[(str(element[0]))] = int(element[1]);


        cur.close();
        conn.close();
    except Exception:
        print("mysql database exception...");
    
    return result;

'''
a = getuserinfo("tom");
b = str(type(a));
print(type(a));
print(a);
'''


