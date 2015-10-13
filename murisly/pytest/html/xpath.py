#coding=utf-8
from lxml import etree

def test():
    fp = open("test_regular.html", "r");
    value = fp.read();
    print(type(value));

    print(value.encode().decode());
    fp.close();
