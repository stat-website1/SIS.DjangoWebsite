from django.shortcuts import render

# Create your views here.
def sitemap_01(request):                                                            #新增
    return render(request,'01_sitemap.html',locals())
