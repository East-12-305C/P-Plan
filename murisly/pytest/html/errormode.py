#coding=UTF-8

import time

def errorWriting(error):
    file = open("error.log", "a");
    nowtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()));
    nowtime = nowtime + "   " + error;
    print(nowtime);
    file.write("\r\n" + nowtime);
    file.close();