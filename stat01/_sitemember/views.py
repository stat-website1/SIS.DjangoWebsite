from django.shortcuts import render

# Create your views here.
def sitemember_01(request):
    return render(request,'sitemember/01_sitemember.html',locals())
