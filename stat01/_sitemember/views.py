from django.shortcuts import render

# Create your views here.
def sitemember_01(request):                 #首頁，暫時用來測試連結之用
    return render(request,'01_sitemember.html',locals())
