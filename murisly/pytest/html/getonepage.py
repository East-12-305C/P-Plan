#coding=UTF-8

from lxml import etree

#special symbol
special_tuple = ("&nbsp;", "&amp;");

#get name, sex, address, weibo context
def getWeiboContext(html):
    '''get name, sex, address, weibo context'''

    # replcae special symbol
    for element in special_tuple:
        html = html.replace(element, " ");

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
        if each is not None:
            urls.append(each);

    return urls;

def add():
    print("test");


