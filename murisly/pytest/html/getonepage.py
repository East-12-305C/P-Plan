#coding=UTF-8

from lxml import etree

#special symbol
special_tuple = ("&nbsp;", "&amp;");

#get name, sex, address, weibo context
def getWeiboContext(html):
    '''get name, sex, address, weibo context'''

    html = html.decode();
    # replcae special symbol
    for element in special_tuple:
        html = html.replace(element, " ");
    html = html.encode();
    selector = etree.HTML(html)

    weibovalue = [];
    content = selector.xpath('//span[@class="ctt"]')
    for each in content:
        if each.text is not None:
            weibovalue.append(each.text);

    return weibovalue;

def getWeiboUrl(html):
    '''get urls from a page'''
    selector = etree.HTML(html);
    urls = [];
    content = selector.xpath('//a/@href')
    for each in content:
        if each is None:
            continue;

        pos = each.find("?");
        if pos != -1:
            continue;

        pos = each.find("http://weibo.cn");
        if pos == -1:
            continue;

        pos = each.find("http://weibo.cn/page");
        if pos != -1:
            continue;

        pos = each.find("http://weibo.cn/topic");
        if pos != -1:
            continue;

        if "http://weibo.cn" == each:
            continue;

    urls = set(urls);
    return urls;

def add():
    print("test");


