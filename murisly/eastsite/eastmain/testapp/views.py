from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
	return HttpResponse("hello everyone, this a test east305c! write by python!");
