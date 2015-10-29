#coding=UTF-8

import pymysql
import collections

g_province = [
    '北京',
    '重庆',
    '天津',
    '吉林',
    '黑龙江',
    '辽宁',
    '陕西',
    '山西',
    '青海',
    '浙江',
    '江苏',
    '江西',
    '安徽',
    '福建',
    '山东',
    '河北',
    '河南',
    '上海',
    '湖北',
    '湖南',
    '广东',
    '广西',
    '海南',
    '四川',
    '贵州',
    '其他',
    '云南',
    '甘肃',
    '内蒙古',
    '海外',
    '西藏',
    '宁夏',
    '台湾',
    '新疆',
    '香港',
    '澳门',
]


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
        
        #地理位置
        addrdict = {};
        num = 0;
        for element in g_province:
            sql = 'select count(*) as value from firstuser where address like "%%%s%%";' % element;
            cur.execute(sql);
            tmp = cur.fetchall();
            num += tmp[0][0];
            addrdict[element] = (tmp[0][0]);
        addrdict["其他"] += total - num;
        
        result["addrdict"] = addrdict;
        
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


