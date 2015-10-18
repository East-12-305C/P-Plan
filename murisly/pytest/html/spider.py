#coding=UTF-8

import requests
from lxml import etree
import getonepage
import url_catch_queue
import bloomfilter
import xpath
import parsehtml
import scriptcontrol
import re
import sys


def test():
    url = "http://weibo.cn/u/509958159/1234561302";
    result = re.search(r'\d{10}', url);
    print(type(result));
    if result is not None:
        print(result.group(0));
    #print(result.group(1));

def main():
    a = parsehtml.ParseHtml();
    a, b = a.exetparse("http://weibo.cn/rmrb");
    print(a);
    print(len(b))



if __name__ == "__main__":
    scriptcontrol.setStop();
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
