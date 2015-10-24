#coding=utf-8

import parsehtml
from lxml import etree
import re

class GetVips():
    '''
    通过排行榜获取众粉丝用户
    '''

    def __init__(self):
        self.urlget = parsehtml.ParseHtml()
        return

    def gettop(self, url, pages, xpath):
        '''
        获得每日排行榜中的信息
        :param url: 需要获取的主url
        :param pages: 需要获取的页数
        :param xpath: xpath配置
        :return: 需要访问的列表
        '''
        nowpage = 1
        ret = [];

        while nowpage <= pages :
            urlre = "%s&page=%d" % (url, nowpage)
            print(urlre)
            html = self.urlget.gethtml(urlre);
            selector = etree.HTML(html);

            info = selector.xpath(xpath);
            for element in info:
                idurl = element.attrib["href"];
                id = re.search(r"\d{10}", idurl)
                if id is not None:
                    ret.append(id.group(0));

            temp = set(ret)
            nowpage += 1

        return set(ret);

    def start(self):

        toplist = self.gettop("http://weibo.cn/pub/top?cat=star", 20, "//tr/td[@valign]/a")
        print(len(toplist));
        return