from django.shortcuts import render

# Create your views here.
def student_01(request):
    return render(request,"01_student.html",locals())

def student_04(request):
 return render(request,"04_student.html",locals())
