#!/usr/bin/python3.2

import re
import urllib.request

ret = urllib.request.urlopen("http://www.baidu.com");
html = ret.read();


pattern = re.compile(r'http://.+?\"');

#file = open("baidu.txt", "w", encoding='utf-8');
#file.write(html.decode());
#file.close();

#print(html.decode())
match = pattern.findall(html.decode());
#match = pattern.findall('123http://s1.bd\"static.comhttp://che/s\"tatic/baihttp://duia_b45d552b.js\",cac');

for x in match: 
    print(x) 
