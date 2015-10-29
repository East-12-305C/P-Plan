
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from testapp.mysqlhelper import *
import collections
import json
from django.utils.safestring import SafeString


def hello(request):
    return HttpResponse("everyone, this a test east305c! write by python!");

def home(request):
    ret = getweibototal();
    weibodict = json.dumps(ret["totaldict"], ensure_ascii=False);
    sexlist = json.dumps(ret["sexdict"], ensure_ascii=False);
    addrlist = json.dumps(ret["addrdict"], ensure_ascii=False);
    print(addrlist);
    return render(request, 'home.html', {"namelist": SafeString(weibodict), "sexlist": SafeString(sexlist), "addrlist": SafeString(addrlist)});

def weibotest(request):
    name = request.GET.get("name");
    if name is None:
        return render(request, 'weibotest.html');
    
    info = getuserinfo(name);      
    print(info);

    if info is None:
        return HttpResponse(str(name) + "is not exist");

    if len(info) < 1:
        return HttpResponse("dont find this user");

    ret = {};
    ret["id"] = info[0][0];
    ret["name"] = info[0][1];
    ret["exist"] = info[0][2];
    ret["follow"] = info[0][3];
    return render_to_response('weiboret.html', ret);
'''
    ret = "the id is:" + str(info[0][0]) + "    the name is:" + str(info[0][1] ) + "        is exist:" + str(info[0][2]) + "        follow is:" + str(info[0][3]);
'''
    #return render(request, 'weiboret.html');
    #return HttpResponse("test");




