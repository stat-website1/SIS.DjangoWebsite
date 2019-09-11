from django.shortcuts import render

# Create your views here.
def teacher_01(request):
    return render(request,"01_teacher.html",locals())

def teacher_02(request):
    return render(request,"02_teacher.html",locals())

def teacher_03(request):
    return render(request,"03_teacher.html",locals())
