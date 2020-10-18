from django.shortcuts import render
from .models import Sketch,Handcraft,Card,Human,Building,Nature,Plant


def home(request):
    s=Sketch.objects.all()

    return render(request,"home.html",{'s':s}) 

# Create your views here.
def handcraft(request):
    s=Handcraft.objects.all()

    return render(request,"artist.html",{'s':s}) 

def plant(request):
    s=Plant.objects.all()

    return render(request,"artist.html",{'s':s}) 

def card(request):
    s=Card.objects.all()

    return render(request,"artist.html",{'s':s}) 

def human(request):
    s=Human.objects.all()

    return render(request,"artist.html",{'s':s}) 

def building(request):
    s=Building.objects.all()

    return render(request,"artist.html",{'s':s}) 

def nature(request):
    s=Nature.objects.all()

    return render(request,"artist.html",{'s':s}) 