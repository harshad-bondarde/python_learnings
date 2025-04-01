from django.http import HttpResponse
from django.shortcuts import render
def home(request):
#    return HttpResponse("Hello you are at home page")
    return render(request,'website/index.html')  #add template dir in settings.py for this 

def about(request):
    return HttpResponse("Hello you are at about page")

def contact(request):
    return HttpResponse("Hello you are at contact page")
