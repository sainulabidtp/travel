from django.http import HttpResponse
from django.shortcuts import render
from . models import *

# Create your views here.

def demo(request):
    obj=Place.objects.all()
    obj2=Team.objects.all()
    return render(request, "index.html",{'result':obj,'teams':obj2})
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")

