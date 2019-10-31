from django.shortcuts import render

# Create your views here.
def contact_01(request):
   return render(request, "01_contact.html", locals())
