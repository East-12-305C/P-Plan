#coding=utf-8

'''
this module is to parase html down by requests
the tools is xpath
'''

import requests
from lxml import etree
import re


#special symbol
special_tuple = ("&nbsp;", "&amp;", "&quot;", "&gt;", "&lt;");


class ParseHtml():
    def __init__(self):
        return ;

    def gethtml(self, url):
        '''
        get html text from url
        :param url: the url
        :return: html text
        '''

        #5992499741#
        #cook = {"Cookie": "_T_WM=48ec7041fc543364f6424622a3992524; SUB=_2A257Dz7iDeTxGeRG7VYW9i_NzTiIHXVY8EKqrDV6PUJbrdANLUPdkW0Dpvzy7xSdMTg8Y4Zo95O42YNPgQ..; gsid_CTandWM=4uoB5e0911Ct5h8dFhSw5c1fP2E"};
        cook = {"Cookie": "_T_WM=67106e8330d7583086a96a27f89bbe78; SUB=_2A257INIzDeTxGeRG7VYW9i_NzTiIHXVY6v57rDV6PUJbrdANLRLVkW03I-hFmxV4_ldVNwl2Nd1mvtWdMg..; gsid_CTandWM=4u3Jfccf1MVC9Qp3wJK5pc1fP2E"};

        # yiwei0244782920@163.com
        #cook = {"Cookie": "_T_WM=67106e8330d7583086a96a27f89bbe78; SUB=_2A257INFzDeTxGeNP6VUV9S3KyjWIHXVY6v87rDV6PUJbvNAKLUPmkW0dLL8g0lXGGMYltZeHPvonNwdcmw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhH-QzAXKFCsAAh-E0gPjhy5JpX5K-t; SUHB=0XD13o1lBtzZK8; SSOLoginState=1445241123"}


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

        url = "http://weibo.cn/" + userid + "/info?retcode=6102";
        html = self.gethtml(url);
        selector = etree.HTML(html);

        userinfo = {};

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

        #print(userinfo);
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

        if user_id is not None:
            user = {};
            user["id"] = user_id;
            user["interes"] = user_interes;
            user["follow"] = user_follow;
            user["weibos"] = user_weibos;
            return user;
        return None;

    def getInterList(self, userid):
        '''
        获得一个用户的关注列表
        :param url: url
        :return:
        '''

        interList = [];
        pagemax = 21;
        nowpage = 1;
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
            userinfo = self.getuserinfo(userid["id"]);
            userinfo["id"] = userid["id"];
            userinfo["follow"] = userid["follow"];
            userinfo["interes"] = userid["interes"];
            userinfo["weibos"] = userid["weibos"];


            interesList = None;
            interesList = set(self.getInterList(userid["id"]));
            return userinfo, interesList;

        return None, None;