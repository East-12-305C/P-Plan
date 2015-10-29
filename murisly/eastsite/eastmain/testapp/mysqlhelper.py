#coding=UTF-8

import pymysql
import collections

def getweibototal():
    totaldict = collections.OrderedDict();
    result = {};
    try:
        conn = pymysql.connect(host='localhost', user='root', passwd='east', db='spider', port=3306, charset="utf8");
        cur = conn.cursor();
        
        #total
        sql = 'select nickname,follow from firstuser order by follow desc limit 20;'
        cur.execute(sql);
        ret = cur.fetchall();
        for element in ret:
            totaldict[(str(element[0]))] = int(element[1]);
        result["totaldict"] = totaldict;
        
        #sex
        sexdict = {};
        sql = 'select count(*) as value from firstuser where sex = 0;'
        cur.execute(sql);
        female = cur.fetchall();
        sexdict["female"] = int(female[0][0]);

        sql = 'select count(*) as value from firstuser where sex = 1;'
        cur.execute(sql);
        male = cur.fetchall();
        sexdict["male"] = int(male[0][0]);

        sql = 'select count(*) as value from firstuser;'
        cur.execute(sql);
        ret = cur.fetchall();
        total = int(ret[0][0]);
        sexdict["other"] = total - int(female[0][0]) - int(male[0][0]);
        result["sexdict"] = sexdict;
        

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


