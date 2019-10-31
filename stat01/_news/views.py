from django.shortcuts import render

# Create your views here.

def news_01(request):                                                            #新增
    return render(request,'01_news.html',locals())
