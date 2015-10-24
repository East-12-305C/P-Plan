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
import timerope



def test():
    special_tuple = ("&nbsp;", "&amp;", "&quot;", "&gt;", "&lt;")
    url = "http://weibo.cn/2803301701"
    cook = {"Cookie": "_T_WM=7267c27f388b035051df7cbf9ca6bc99; SUB=_2A257LKYcDeTxGeNP6VUQ-SbEzDyIHXVY7spUrDV6PUJbvNBeLUzjkW1uG3XlV-dJ0mkcWoH3t7PLEDqlXQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF.0-J5o-HaXmNuGucM2qWQ5JpX5K-t; SUHB=0V51LM5pvDrm8m; SSOLoginState=1445516876"};
    html = requests.get(url, cookies = cook).text   #get str


    # replcae special symbol
    for element in special_tuple:
        html = html.replace(element, " ");

    html = html.encode();
    selector = etree.HTML(html);
    title = selector.xpath('//head/title/text()');
    print(len(title))
    title = title[0][0:len(title)-4];
    print(title)

    info = selector.xpath('//td/div/span[@class="ctt"]/text()');
    for element in info:
        temp = str(element)
        temp = temp.replace(title, "")
        temp = temp.replace(" ", "")
        pos = temp.find("/");
        if pos >= 0 :
            sex = temp[0:pos];
            address = temp[pos + 1:];
            print(sex);
            print(address);

    A = 1

def main():
    scriptcontrol.setStart()
    urlqueue = url_catch_queue.UrlQueue()
    urlget = parsehtml.ParseHtml()
    exceptTimes = 0
    while scriptcontrol.isContinue():
    #while exceptTimes < 2:
        exceptTimes += 1
        try:
            userid = urlqueue.geturl()

            if userid is None:
                url = "http://weibo.cn/rmrb"
                url = "http://weibo.cn/1291477752";
            else:
                url = "http://weibo.cn/%s" % userid

            print(url);

            info, urllist = urlget.exetparse(url);
            #info = {'weibos': '52780', 'id': '2803301701', 'follow': '40001594', 'sex': '1', 'birthday': '19480615', 'interes': '1249', 'address': '北京', 'nickname': '人民日报'}
            #urllist = {'1642591402', '1894467483', '2737798435', '3011694992', '2618638282', '2192630467', '3363206842', '3183107112', '1726918143', '2641686425', '1893801487', '1642512402', '1644948230'}

            if info is None:
                print(url + " no visit")
                urlqueue.inserturl(list(userid));
            else:
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


def setTimer():
    liking = timerope.GetVips();
    liking.start();
    return 0

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
            scriptcontrol.setStop();
        elif sys.argv[1] == "search":
            setTimer();
        else:
            print("param error")
    else:
        print("param error")
