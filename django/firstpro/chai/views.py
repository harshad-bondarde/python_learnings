#built using python manage.py startapp chai

from django.shortcuts import render

# Create your views here.

def all_chai(request):
    return render(request,'chai/all_chai.html')
def order(request):
    return render(request,'chai/order.html')