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



def test( a, b, *param ):


    i = 1;
    urlqueue = url_catch_queue.UrlQueue();
    while i < 100:

        urlqueue.inserturl(str(i));
        i += 1;

    urlqueue.stop();


def main():
    return 0;
    scriptcontrol.setStart();
    urlqueue = url_catch_queue.UrlQueue();
    exceptTimes = 0;
    #while scriptcontrol.isContinue():
    while exceptTimes < 1 :
        exceptTimes += 1;
        try:
            url = urlqueue.geturl();

            if url is None:
                url = "http://weibo.cn/rmrb";

            a = parsehtml.ParseHtml();
            #info, b = a.exetparse(url);
            #print(type(info));
            #print((info));

            #for interes in b :
            #    urlqueue.inserturl(interes);


        except Exception :
            nowtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()));
            exceptTimes += 1;
            print("main exception time: " + nowtime);
            print("main exception time: " + str(exceptTimes));

    urlqueue.stop();


def fablac(n):
    return n + 1;



if __name__ == "__main__":
    test(fablac,2,3,4,5);
    '''
    scriptcontrol.setStart();
    paramlen = (len(sys.argv));
    print("param num is : " + str(paramlen));
    if paramlen < 2:
        main();
    elif paramlen == 2 :
        if sys.argv[1] == "start" :
            main();
        elif sys.argv[1] == "stop" :
            main();
        else :
            print("param error");
    else :
        print("param error");
    '''
