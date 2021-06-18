
from datetime import datetime, time
from django import http
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.views.decorators.http import require_http_methods

def fun(request):
    return render(request,"demo.html")
def Home(request):

    return render(request,"index1.html")



@require_http_methods(["GET","POST"])    
def fun1(request):
    return HttpResponse("welcome")   

def fun2(request,number):
    return HttpResponse(f"the time is{number}")   

    

# Create your views here.
