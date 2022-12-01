from multiprocessing import context
from django.shortcuts import render
from .models import *
# Create your views here.
def landing(request):
    duyurular=Duyuru.objects.all().order_by("-id")
    context={
        'duyurular':duyurular
    }
    return render(request,"landing.html",context)

def duyurr(request, duyuruId):
    duyurular=Duyuru.objects.filter(baslik = duyuruId)
    context={
        'duyurular':duyurular
    }
    return render(request,"duyuru.html",context)

def iletisim(request):
    return render(request,"iletisim.html")

def hakkimizda(request):
    return render(request,"hakkimizda.html")

def stigma(request):
    return render(request,"stigma.html")

def derinMevzu(request):
    return render(request,"derinmevzu.html")


def mentalhealth101(request):
    return render(request,"mentalhealth101.html")