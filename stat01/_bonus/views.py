from django.shortcuts import render

# Create your views here.
def bonus_04(request):
    return render(request,"04_bonus.html",locals())

def bonus_05(request):                                                            
    return render(request,"05_bonus.html",locals())

def bonus_07(request):                                                            
    return render(request,"07_bonus.html",locals())
