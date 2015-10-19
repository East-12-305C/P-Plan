#coding=UTF-8

import requests
from lxml import etree
import url_catch_queue
import bloomfilter
import parsehtml
import scriptcontrol
import re
import sys
import time


def test():
    a= "微博[4321]";
    b = re.search(r'(\d+)', a);
    print(b.group(0));


def main():
    scriptcontrol.setStart();
    #urlqueue = url_catch_queue.UrlQueue();
    exceptTimes = 0;
    while scriptcontrol.isContinue():
        #try:
        #url = urlqueue.geturl();
        url = None;
        if url is None:
            url = "http://weibo.cn/rmrb";

        a = parsehtml.ParseHtml();
        info, b = a.exetparse(url);
        print(info);

        #for interes in b :
        #    urlqueue.inserturl(interes);


        #except Exception :
        '''
            nowtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()));
            exceptTimes += 1;
            print("main exception time: " + nowtime);
            print("main exception time: " + str(exceptTimes));
            '''




if __name__ == "__main__":
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
