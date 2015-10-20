#coding=UTF-8

import requests
from lxml import etree
import url_catch_queue
import bloomfilter
import parsehtml
import scriptcontrol
import errormode
import re
import sys
import time
import pymysql



def test():
    connect = pymysql.connect(host='localhost',user='root',passwd='east',db='spider',port=3306, charset="gbk")
    cursor = connect.cursor()

    userinfo = {'weibos': '52780', 'id': '0331701', 'follow': '40001594', 'sex': '1', 'birthday': '19480615', 'interes': '1249', 'address': '北京', 'nickname': '人民日报'}
    id = userinfo["id"]
    nickname = userinfo["nickname"]
    sex = userinfo["sex"]
    address = userinfo["address"]
    birthday = userinfo["birthday"]
    weibos = userinfo["weibos"]
    follow = userinfo["follow"]
    interes = userinfo["interes"]
    sql = "insert firstuser values(%s,'%s',%s,'%s',%s,%s,%s,%s) ON DUPLICATE KEY UPDATE nickname='%s',sex=%s,address='%s',birthday=%s,weibos=%s,follow=%s,interes=%s;" % (id,nickname,sex,address,birthday,weibos,follow,interes, nickname,sex,address,birthday,weibos,follow,interes);
    print(sql)
    cursor.execute(sql)
    connect.commit()

    cursor.close()
    connect.close()


def main():
    scriptcontrol.setStart()
    urlqueue = url_catch_queue.UrlQueue()
    exceptTimes = 0
    #while scriptcontrol.isContinue():
    while exceptTimes < 5:
        exceptTimes += 1
        try:
            userid = urlqueue.geturl()
            url = None

            if userid is None:
                url = "http://weibo.cn/rmrb"
            else:
                url = "http://weibo.cn/%d" % userid

            a = parsehtml.ParseHtml()
            #info, urllist = a.exetparse(url);
            info = {'weibos': '52780', 'id': '2803301701', 'follow': '40001594', 'sex': '1', 'birthday': '19480615', 'interes': '1249', 'address': '北京', 'nickname': '人民日报'}
            urllist = {'1642591402', '1894467483', '2737798435', '3011694992', '2618638282', '2192630467', '3363206842', '3183107112', '1726918143', '2641686425', '1893801487', '1193725273', '2616293707', '2781790222', '1722022490', '5031100920', '3292292327', '1220291284', '1977460817', '5053469079', '1991123083', '1775895885', '1496852380', '3756087501', '5065477686', '1653076903', '3201725574', '1896650227', '2053061043', '1640601392', '3587960280', '1686546714', '1420157965', '5208067255', '2577039065', '2282929711', '1774835215', '1700648435', '1784473157', '1961594843', '1578818417', '1638782947', '2818156631', '1656737654', '1708763410', '1663937380', '2806187513', '3802136340', '2089358175', '3037284894', '5182171545', '2493592183', '1651428902', '2258833123', '2384122784', '1288369910', '2998045524', '3120845115', '1232121710', '3506728370', '1652484947', '2635157384', '3535242221', '2662494703', '2501519087', '3356940544', '1645578093', '2748597475', '3957042973', '1529573474', '3288875501', '2719969734', '5608433557', '1649173367', '5476386628', '1880295725', '3057540037', '2280198017', '5361563575', '1990226474', '2372649470', '2827102952', '2571494540', '1935167034', '2938715943', '1644489953', '3230238400', '1663072851', '1198367585', '3649546555', '1664971205', '1700720163', '3549916270', '1655444627', '3785786395', '2043228245', '1643971635', '1653689003', '3514732862', '5044281310', '2639029341', '1623340585', '3508612897', '2275883675', '5000609535', '2699180811', '1990533882', '2244639353', '1644114654', '2993049293', '2920787694', '3908755088', '1917433500', '3163782211', '3403473360', '2753006425', '2087169013', '2011075080', '1735882701', '3494982177', '1887790981', '1985636721', '2778606994', '5099581595', '1910577521', '1642088277', '2544191434', '5149608258', '1642482194', '2388955087', '2302688157', '2927573465', '1768541657', '1734530730', '1720962692', '2417139911', '2244525523', '2245075615', '3225138431', '1701600025', '1641532820', '1904228041', '1231759973', '2443744521', '5070395229', '5186027114', '3481045492', '1641561812', '2431328567', '3881380517', '2516831703', '2807295185', '1663148275', '1898268644', '5386897742', '2848929290', '3044746573', '5039061087', '2210168325', '3043581645', '3921015143', '1765891182', '2974325495', '3687019147', '1701367442', '1497087080', '2374457344', '3535465954', '1222135407', '1867571077', '2243807243', '1192329374', '1623842133', '3921730119', '1697601814', '2752396553', '3071103322', '3499010272', '1655363172', '3546332963', '3204782330', '2294165474', '2525973044', '1314608344', '2271051770', '3114175427', '5049237517', '1792702427', '1653603955', '1103147195', '2117508734', '2176235777', '1882716230', '1682207150', '1419172372', '3937348351', '3097688767', '1113218211', '1642512402', '1644948230'}

            print((info))

            urlqueue.updateAlluser(info)
            if int(info["follow"]) > 1000000:
                urlqueue.updateFirstuser(info)

            if urllist is not None:
                for interes in urllist :
                    urlqueue.inserturl(interes)


        except Exception :
            nowtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
            exceptTimes += 1
            print("main exception time: " + nowtime)
            print("main exception time: " + str(exceptTimes))

    urlqueue.stop()



if __name__ == "__main__":

    scriptcontrol.setStart()
    paramlen = (len(sys.argv))
    print("param num is : " + str(paramlen))
    if paramlen < 2:
        main()
    elif paramlen == 2:
        if sys.argv[1] == "start":
            main()
        elif sys.argv[1] == "stop":
            main()
        else:
            print("param error")
    else:
        print("param error")

