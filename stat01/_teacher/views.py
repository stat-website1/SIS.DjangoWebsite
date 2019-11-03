from django.shortcuts import render

def teacher_01(request):
    return render(request,"teacher/01_teacher.html",locals())

def teacher_02(request):
    return render(request,"teacher/02_teacher.html",locals())

def teacher_03(request):
    return render(request,"teacher/03_teacher.html",locals())
