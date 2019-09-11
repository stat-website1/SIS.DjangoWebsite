from django.shortcuts import render

# Create your views here.

def index(request):
    section={"title":"title"}
    return render(request,"index.html",locals())

def research_01(request):
    return render(request,"01_research.html",locals())

def research_02(request):
    return render(request,'02_research.html',locals())

def research_03(request):
    return render(request,"03_research.html",locals())

def research_04(request):
    return render(request,"04_research.html",locals())


