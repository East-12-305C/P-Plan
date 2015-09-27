
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse("hello everyone, this a test east305c! write by python!");

def home(request):
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    welfunc = "this is a conbine!";
    return render(request, 'home.html', {"namelist": TutorialList});
