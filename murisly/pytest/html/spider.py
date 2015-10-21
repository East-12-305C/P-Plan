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
    connect = pymysql.connect(host='localhost',user='root',passwd='east',db='spider',port=3306, charset="gbk")
    cursor = connect.cursor()

    userinfo = {'weibos': '52780', 'id': '0331701', 'follow': '40001594', 'sex': '1', 'birthday': '19480615', 'interes': '1249', 'address': '北京', 'nickname': '人民日报'}
    id = userinfo["id"]
    nickname = userinfo["nickname"]
    sex = userinfo["sex"]
    address = userinfo["address"]
    birthday = userinfo["birthday"]
    weibos = userinfo["weibos"]
    follow = userinfo["follow"]
    interes = userinfo["interes"]
    sql = "insert firstuser values(%s,'%s',%s,'%s',%s,%s,%s,%s) ON DUPLICATE KEY UPDATE nickname='%s',sex=%s,address='%s',birthday=%s,weibos=%s,follow=%s,interes=%s;" % (id,nickname,sex,address,birthday,weibos,follow,interes, nickname,sex,address,birthday,weibos,follow,interes);
    print(sql)
    cursor.execute(sql)
    connect.commit()

    cursor.close()
    connect.close()


def main():
    scriptcontrol.setStart()
    urlqueue = url_catch_queue.UrlQueue()
    exceptTimes = 0
    while scriptcontrol.isContinue():
    #while exceptTimes < 10:
        exceptTimes += 1
        try:
            userid = urlqueue.geturl()

            if userid is None:
                url = "http://weibo.cn/rmrb"
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
