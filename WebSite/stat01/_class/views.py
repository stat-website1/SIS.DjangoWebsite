from django.shortcuts import render

# Create your views here.
def class_01(request):                                                            #新增
    return render(request,'01_class.html',locals())
