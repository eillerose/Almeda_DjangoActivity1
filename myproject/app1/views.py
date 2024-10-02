from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Renders the index.html template in app1/templates/app1/
    return render(request, 'app1/index.html')  # Ensure the path to your template is correct

def page1(request):
    return HttpResponse("Welcome to App1's Page 1!")

def page2(request):
    return HttpResponse("Welcome to App1's Page 2!")
