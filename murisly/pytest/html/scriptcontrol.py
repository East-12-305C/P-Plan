#coding=UTF-8


def setStop():
    file = open("control", "w");
    file.write("stop");
    file.close();


def isContinue():
    file = open("control", "r");
    file.write("stop");
    file.close();