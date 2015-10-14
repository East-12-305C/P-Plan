#coding=UTF-8

from lxml import etree

#special symbol
special_tuple = ("&nbsp;", "&amp;", "&quot;", "&gt;", "&lt;");

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
    #content = selector.xpath('//div/div/span[@class="cmt"]/../span[@class="ctt"]/text()');
    #content = selector.xpath('//div/div/span[@class="ctt"]/text()');
    content = selector.xpath('//body/div[@id]');

    for each in content:
        if each is not None:
            #a = each.xpath("//div[@id=%s]/span[@class='ctt']/text()" % each.attrib["id"]);
            a = each.xpath("./div/span[@class='ctt']/text()");
            print(''.join(a));
            #a = each.xpath('//body/div[@id]'):
            #print(each.attrib["id"]);
            #each.xpath()
            #print(type(each))
            #weibovalue.append(each);

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

        urls.append(each);

    urls = set(urls);
    return urls;

def add():
    print("test");


