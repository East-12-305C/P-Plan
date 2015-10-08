#coding=UTF-8

import requests
import chardet
from lxml import etree

special_tuple = ("&nbsp;", "&amp;");


cook = {"Cookie": "_T_WM=48ec7041fc543364f6424622a3992524; SUB=_2A257Dz7iDeTxGeRG7VYW9i_NzTiIHXVY8EKqrDV6PUJbrdANLUPdkW0Dpvzy7xSdMTg8Y4Zo95O42YNPgQ..; gsid_CTandWM=4uoB5e0911Ct5h8dFhSw5c1fP2E"};
url = 'http://weibo.cn/u/1931534830' #
#url = 'http://weibo.cn/hanhan';
# html = requests.get(url).content



#html = requests.get(url, cookies = cook).content   #get byte
#print(chardet.detect(html))  #detect code way
html = requests.get(url, cookies = cook).text   #get str


# replcae special symbol
for element in special_tuple:
    html = html.replace(element, " ");


#change code way
html = bytes(bytearray(html, encoding='utf-8'))
selector = etree.HTML(html)


content = selector.xpath('//span[@class="ctt"]')
for each in content:
    if each.text is not None:
        print(each.text)



