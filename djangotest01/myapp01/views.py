from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random
def hello(request):
    return HttpResponse("Django 我來囉!")
    
def hello2(request,username):
    return HttpResponse(str(username)+"歡迎來到Django")


def hello3(request,username):
    now = datetime.now()
    return render(request,"hello3.html",locals())
    
def hello4(request,username):
    now = datetime.now()
    return render(request,"hello4.html",locals())
# Create your views here.


def dice(request):
    no1 = random.randint(1,99)
    no2 = random.randint(1,99)
    no3 = random.randint(1,99)
    return render(request,"dice.html",locals())
    
def show(request):
    person1={"name":"鄭詠升","phone":"0989787808","age":27}
    person2={"name":"邱禹寰","phone":"0989787809","age":26}
    person3={"name":"鄭秋葵","phone":"0989787810","age":0}
    persons=[person1,person2,person3]
    return render(request,"show.html",locals())
    
def djget(request):
    name = request.GET['name']
    city = request.GET['city']
    return render(request,'djget.html',locals())
    
def djpost(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'zheng' and password =='0522':
            return HttpResponse('帳號密碼答對囉')
        else:
            return HttpResponse('帳號密碼錯誤')
    else:
        return render(request,'djpost.html',locals())