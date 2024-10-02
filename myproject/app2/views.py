from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to App2's homepage!")

def page1(request):
    return HttpResponse("Welcome to App2's Page 1!")

def page2(request):
    return HttpResponse("Welcome to App2's Page 2!")
