
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from testapp.mysqlhelper import *

def hello(request):
    return HttpResponse("everyone, this a test east305c! write by python!");

def home(request):
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    welfunc = "this is a conbine!";
    return render(request, 'home.html', {"namelist": TutorialList});

def weibotest(request):
    name = request.GET.get("name");
    if name is None:
        return render(request, 'home.html');
    
    info = getuserinfo(name);
    print("second:")        
    print(info);

    if info is None:
        return HttpResponse(str(name) + "is not exist");

    if len(info) < 0:
        return HttpResponse("dont find this user");

    ret = "the id is:" + str(info[0][0]) + "    the name is:" + str(info[0][1] ) + "        is exist:" + str(info[0][2]) + "        follow is:" + str(info[0][3]);
    return HttpResponse(ret);
