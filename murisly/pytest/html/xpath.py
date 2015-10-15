#coding=utf-8
from lxml import etree



def test():
    fp = open("test_regular.html", "rb");
    html = fp.read();

    selector = etree.HTML(html);
    content = selector.xpath('//ul[@id="useful"]/text()')

    print(type(content)); #//*[@id="content"]
    print(len(content));
    for element in content:
        a = "".join(element.split());
        print(a)
        # for name in element.attrib:
        #     print((name));

    fp.close();


def getnodevalue():
    fp = open("test_regular.html", "rb");
    html = fp.read();

    selector = etree.HTML(html);
    content = selector.xpath('//li')   #获得li下的所有内容值

    print(type(content)); #//*[@id="content"]
    print(len(content));
    for element in content:
        print(type(element));
        print(element.text);

    fp.close();