from django.shortcuts import render

# Create your views here.
def index(request):                 #首頁，暫時用來測試連結之用
    section={'title':'title'}
    return render(request,'index.html',locals())

def about_01(request):                                                            #新增
    return render(request,'01_about.html',locals())

def about_03(request):
    return render(request,"03_about.html",locals())

def about_04(request):
    return render(request,'04_about.html',locals())

def about_05(request):
    return render(request,"05_about.html",locals())

def about_07(request):
    return render(request,"07_about.html",locals())
