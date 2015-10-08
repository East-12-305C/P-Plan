#coding=UTF-8

import requests
import chardet
from lxml import etree

special_tuple = ("&nbsp;", "&amp;");


cook = {"Cookie": "_T_WM=48ec7041fc543364f6424622a3992524; SUB=_2A257Dz7iDeTxGeRG7VYW9i_NzTiIHXVY8EKqrDV6PUJbrdANLUPdkW0Dpvzy7xSdMTg8Y4Zo95O42YNPgQ..; gsid_CTandWM=4uoB5e0911Ct5h8dFhSw5c1fP2E"};
url = 'http://weibo.cn/u/1931534830' #
#url = 'http://weibo.cn/hanhan';
# html = requests.get(url).content

print(special_tuple);



#html = requests.get(url, cookies = cook).content
#print(chardet.detect(html))
html = requests.get(url, cookies = cook).text
print(html);

for element in special_tuple:
    html = html.replace(element, " ");

html = bytes(bytearray(html, encoding='utf-8'))
print(html);
selector = etree.HTML(html)



#print((selector[0].tag));
#print((selector[1].tag));
content = selector.xpath('//span[@class="ctt"]')

file = open("test.txt", "wb");

for each in content:
    if each.text is not None:
        encodetype = chardet.detect((each.text).encode("gbk", 'ignore'));
        #gbkcode = ((each.content).encode("utf-8", 'ignore'));

        if encodetype["encoding"] == "ISO-8859-2":
            sub = ((each.text).encode("GB18030", "ignore"));
            print(sub);
            print(each.text)
            # print(chardet.detect(sub));
            # (sub.decode("utf-8", "ignore"));
            file.write(sub);
            # new = sub.decode();
            # print(type(gbkcode));
            # print(gbkcode)
            # subtype = chardet.detect(gbkcode);
            # print(subtype);
            #print(gbkcode.decode("ISO-8859-2"));
        else:
            print(each.text)


file.close();

