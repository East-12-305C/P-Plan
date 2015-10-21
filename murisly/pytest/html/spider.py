#coding=UTF-8

import requests
from lxml import etree
import url_catch_queue
import bloomfilter
import parsehtml
import scriptcontrol
import errormode
import re
import sys
import time
import pymysql



def test():
    sql = 'insert alluser values(11, "四大皆空降温哦好");'
    #gbkstr = sql.encode().decode("utf-8");

    try:
        conn = pymysql.connect(host = 'localhost', user = 'root', passwd = 'east', db = 'spider', port=3306, charset="utf8")
        cur = conn.cursor()

        #cur.execute("create table %s(id bigint(10) not null auto_increment, nickname char(32) not null, PRIMARY KEY(id))" % "alluser");
        print(sql)
        cur.execute(sql)

        conn.commit()
        cur.close()
        conn.close()

    except Exception:
        print("exception...")


def main():
    return 0;
    scriptcontrol.setStart()
    urlqueue = url_catch_queue.UrlQueue()
    exceptTimes = 0
    #while scriptcontrol.isContinue():
    while exceptTimes < 1:
        exceptTimes += 1
        try:
            userid = urlqueue.geturl()

            if userid is None:
                url = "http://weibo.cn/rmrb"
                url = "http://weibo.cn/2100294813?retcode=6102";
            else:
                url = "http://weibo.cn/%s" % userid

            a = parsehtml.ParseHtml()
            info, urllist = a.exetparse(url);
            #info = {'weibos': '52780', 'id': '2803301701', 'follow': '40001594', 'sex': '1', 'birthday': '19480615', 'interes': '1249', 'address': '北京', 'nickname': '人民日报'}
            #urllist = {'1642591402', '1894467483', '2737798435', '3011694992', '2618638282', '2192630467', '3363206842', '3183107112', '1726918143', '2641686425', '1893801487', '1642512402', '1644948230'}

            urlqueue.updateAlluser(info)
            if int(info["follow"]) > 1000000:
                urlqueue.updateFirstuser(info)

            if urllist is not None:
                for interes in urllist:
                    urlqueue.inserturl(interes)
        except Exception:
            nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            exceptTimes += 1
            print("main exception time: " + nowtime + " " + str(userid));

    urlqueue.stop()

if __name__ == "__main__":
    test();
    scriptcontrol.setStart()
    paramlen = (len(sys.argv))
    print("param num is : " + str(paramlen))
    if paramlen < 2:
        main()
    elif paramlen == 2:
        if sys.argv[1] == "start":
            main()
        elif sys.argv[1] == "stop":
            main()
        else:
            print("param error")
    else:
        print("param error")
