#coding=UTF-8

import requests
from lxml import etree
import getonepage
import url_catch_queue
import bloomfilter
import xpath


def test():
    base = "http://www.weibo.cn/%s";
    urlqueue = url_catch_queue.UrlQueue();
    urlqueue.inserturl(base % "8")

def inserturl():
    i = 0;
    base = "http://www.weibo.cn/%s";
    urlqueue = url_catch_queue.UrlQueue();
    while i < 20:
        urlqueue.inserturl(base % str(i));
        i += 1;


def geturl():
    urlqueue = url_catch_queue.UrlQueue();
    while True:
        url = urlqueue.geturl();
        if url is None:
            break;

        print(url);

    return 0;

def main():

    cook = {"Cookie": "_T_WM=48ec7041fc543364f6424622a3992524; SUB=_2A257Dz7iDeTxGeRG7VYW9i_NzTiIHXVY8EKqrDV6PUJbrdANLUPdkW0Dpvzy7xSdMTg8Y4Zo95O42YNPgQ..; gsid_CTandWM=4uoB5e0911Ct5h8dFhSw5c1fP2E"};
    url = 'http://weibo.cn/rmrb' #
    #url = 'http://weibo.cn/2864761164/follow';
    # html = requests.get(url).content


    html = requests.get(url, cookies = cook).content   #get byte
    #html = requests.get(url, cookies = cook).text   #get str


    #change code way
    #html = bytes(bytearray(html, encoding='utf-8'))

    weibovalue = getonepage.getWeiboContext(html);
    for element in weibovalue:
        print(element);

    context = getonepage.getWeiboUrl(html);
    for element in context:
        print(element);


#test();

#geturl();

#inserturl();

#main();

xpath.test();


