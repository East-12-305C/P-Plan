#!/usr/bin/python3.2

import re

pattern = re.compile(r'http://.+\"');

#file = open("baidu.txt", "r");
#value = file.read();
#file.close();

match = pattern.match('http://www.baidu.com\"sdfas');

if match:
    print(match.group());


