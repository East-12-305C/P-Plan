#coding=utf-8

'''
this module is to parase html down by requests
the tools is xpath
'''


class ParseHtml():
    def __init__(self):
        return None;

    def gethtml(self, url):
        '''
        get html text from url
        :param url: the url
        :return: html text
        '''
        return 0;

    def getuserinfo(self, html):
        '''
        get user info from the current html text
        :param html: current html text
        :return: user info
        {
            "id": "idnum",
            "nickname": "jack",
            "sex": "male";
            "birthday": "19880901"
            "address": "beijing",
        }
        '''
        return 0;

    def getweibocontext(self, html):
        '''
        get weibo text from html
        :param html:
        :return: weibo info
        {
            "context": "weibo context",
            "postday": "20150102", #year month day
            "posttime": "1503", #post time
            "isforward": "1", #1 is forword, 0 is not
            "comment": "1236", #how many people comment it
            "zans": "2345", how many people zans it
        }
        '''

        return 0;


    def exetparse(self, url = "http://weibo.cn"):
        '''
            this function is to parse html
        :param url: the url get
        :return:nil name, sex, address, age, weibo context,
        '''
        return 1, 2;