#coding=utf-8

'''
this module is to parase html down by requests
the tools is xpath
'''

import requests
from lxml import etree
import re
import time


#special symbol
special_tuple = ("&nbsp;", "&amp;", "&quot;", "&gt;", "&lt;");


class Cookies():
    def __init__(self):

        self.cook = (
            #5992499741
            #{"Cookie": "_T_WM=9c995b353baf09efb0dd45642f0f9bf4; SUB=_2A257KjpxDeTxGeRG7VYW9i_NzTiIHXVY1UY5rDV6PUJbrdAKLXnHkW1WePUF73f4htpm35-AjgeG0Z5d8A..; gsid_CTandWM=4uIgfccf1TmCeFHMrXS1Yc1fP2E"},
            #shajiayechao3@163.com
            #{"Cookie": "_T_WM=9c995b353baf09efb0dd45642f0f9bf4; SUB=_2A257LpZiDeTxGeNP6VUV9S3KyTiIHXVY0DoqrDV6PUJbvNBeLXfXkW0TZOK2CESM9XfkZjDBI7Z2wpzDHA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF8dy3ua7XqE.c6EyrNNvu-5JpX5K-t; SUHB=0mxEJjAg6WhhWs; SSOLoginState=1445652019"},
            #tezhong69239@163.com
            #{"Cookie": "_T_WM=7267c27f388b035051df7cbf9ca6bc99; SUB=_2A257L8R2DeTxGeNP6VUQ-SbEzT2IHXVY0-w-rDV6PUJbvNANLWrbkW1TSpJsY6WEsn_TN2wEVGfAPnBv3w..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWL6A.u2VkuC0YVxrvvdvhd5JpX5K-t; SUHB=0M2Vo3Kp6M1IT0; SSOLoginState=1445704742"},
            #xie814403@163.com
            {"Cookie": "_T_WM=9c995b353baf09efb0dd45642f0f9bf4; SUHB=0nl-NdMXIlJsPS; SUB=_2A257NZj8DeTxGeRG7VYW9i_NzTiIHXVY2Ti0rDV6PUJbrdAKLXn1kW2KraJvoarfW_xaVB9FbIAbg0VwUQ..; gsid_CTandWM=4u15fccf1ycdqnJTQDwzuc1fP2E"},
        )

        self.pos = 0;
        self.length = len(self.cook);

    def getCook(self):
        self.pos += 1;
        if self.pos >= self.length :
            self.pos = 0;

        return self.cook[self.pos];




class ParseHtml():
    def __init__(self):
        self.CookCreate = Cookies();
        return ;

    def gethtml(self, url):
        '''
        get html text from url
        :param url: the url
        :return: html text
        '''

        time.sleep(0.4);
        cook = self.CookCreate.getCook();

        proxies = {
            "https": "http://220.248.224.242:8089",
        }


        #html = requests.get(url, cookies = cook, proxies=proxies).text   #get str
        html = requests.get(url, cookies = cook).text   #get str


        # replcae special symbol
        for element in special_tuple:
            html = html.replace(element, " ");

        html = html.encode();
        return html;

    def getsubinfo(self, src, findtext):
        '''
        提取用户的信息
        :param src: 原始字符串
        :param findtext: 查找的字符串
        :return: 需要的信息
        '''
        if src.find(findtext) >= 0 :
            return src[len(findtext) : ];
        return None;


    def getuserinfo(self, userid):
        '''
        get user info from the current html text
        :param userid: current user id
        :return: user info
        {
            "id": "idnum",
            "nickname": "jack",
            "sex": "male";
            "birthday": "19880901"
            "address": "beijing",
        }
        '''

        url = "http://weibo.cn/" + userid + "/info";
        html = self.gethtml(url);
        selector = etree.HTML(html);

        userinfo = {};
        userinfo["nickname"] = "########";
        userinfo["sex"] = "4";
        userinfo["address"] = "unknow";
        userinfo["birthday"] = "0";

        info = selector.xpath('//body/div/text()');
        for element in info:
            length = len(element);
            if length < 3 :
                continue;


            temp = (self.getsubinfo(element, "昵称:"));
            if temp is not None:
                userinfo["nickname"] = temp;

            temp = (self.getsubinfo(element, "性别:"));
            if temp is not None:
                if temp == "女" :
                    userinfo["sex"] = "0";
                elif temp == "男" :
                    userinfo["sex"] = "1";
                else :
                    userinfo["sex"] = "2";
            else:
                userinfo["sex"] = "3";

            temp = (self.getsubinfo(element, "地区:"));
            if temp is not None:
                userinfo["address"] = temp;

            temp = (self.getsubinfo(element, "生日:"));
            if temp is not None:
                userinfo["birthday"] = temp.replace("-", "");


        return userinfo;

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

    def getuserid(self, html):
        '''
        get user id(a number), interest, follow;
        :param html:
        :return:
        '''
        user_id = None;
        user_follow = 0;
        user_interes = 0;
        user_weibos = 0;

        selector = etree.HTML(html);

        content = selector.xpath('//td[@valign="top"]/div[@class="ut"]/a');
        for element in content:
            if element.text == "资料":
                user_id = (element.attrib["href"][1:11]);

        weibonum = selector.xpath('//div[@class="u"]/div[@class="tip2"]/span/text()');
        if len(weibonum) > 0 :
            num = re.search(r'\d+', weibonum[0]);
            if num is not None:
                user_weibos = num.group(0);

        follow = selector.xpath('//div[@class="u"]/div[@class="tip2"]/a');
        for element in follow:
            if element.text.find("关注") >= 0:
                start = element.text.find("[");
                end = element.text.find("]");
                user_interes = (element.text[start+1:end]);
            elif element.text.find("粉丝") >= 0:
                start = element.text.find("[");
                end = element.text.find("]");
                user_follow = (element.text[start+1:end]);

        nickname = selector.xpath('//head/title/text()');
        nickname = nickname[0][0:len(nickname)-4];

        sex = 4;
        address = "unknow"
        info = selector.xpath('//td/div/span[@class="ctt"]/text()');
        for element in info:
            temp = str(element)
            temp = temp.replace(nickname, "")
            temp = temp.replace(" ", "")
            pos = temp.find("/");
            if pos >= 0 :
                sex = temp[0:pos];
                address = temp[pos + 1:];
                if sex.find("男") >= 0:
                    sex = 1;
                elif sex.find("女") >= 0:
                    sex = 0;


        if user_id is not None:
            user = {};
            user["id"] = user_id;
            user["interes"] = user_interes;
            user["follow"] = user_follow;
            user["weibos"] = user_weibos;
            user["nickname"] = nickname;
            user["sex"] = sex;
            user["address"] = address;
            return user;
        return None;

    def getInterList(self, userid):
        '''
        获得一个用户的关注列表
        :param url: url
        :return:
        '''

        interList = [];
        pagemax = 6;
        nowpage = 3;
        while nowpage < pagemax:
            url = "http://weibo.cn/" + userid + "/follow?page=" + str(nowpage);
            html = self.gethtml(url);
            selector = etree.HTML(html);

            interest = selector.xpath('//table/tr/td[@valign="top"]/a');
            for element in interest:
                temp = element.attrib["href"];
                result = re.findall("\d{10}", temp);
                for id in result:
                    interList.append(id);

            interest = selector.xpath('//table/tr/td[@valign="top"]/a/img');
            for element in interest:
                temp = element.attrib["src"];
                result = re.search("\d{10}", temp);
                if result is not None:
                    interList.append(result.group(0));

            nowpage += 1;

        return interList;

    def exetparse(self, url = "http://weibo.cn"):
        '''
            this function is to parse html
        :param url: the url get
        :return:nil name, sex, address, age, weibo context,
        '''

        html = self.gethtml(url);
        userid = self.getuserid(html);

        if userid is not None:
            userid["birthday"] = 0
            # userinfo = self.getuserinfo(userid["id"]);
            # userinfo["id"] = userid["id"];
            # userinfo["follow"] = userid["follow"];
            # userinfo["interes"] = userid["interes"];
            # userinfo["weibos"] = userid["weibos"];


            interesList = None;
            interesList = set(self.getInterList(userid["id"]));
            return userid, interesList;

        return None, None;
