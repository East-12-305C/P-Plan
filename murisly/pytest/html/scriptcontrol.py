#coding=UTF-8


def setStop():
    file = open("control", "w");
    file.write("stop");
    file.close();

def setStart():
    file = open("control", "w");
    file.write("start");
    file.close();

def isContinue():
    file = open("control", "r");
    temp = file.read();
    file.close();

    if temp.find("start") >= 0 :
        return True;
    else :
        return False;