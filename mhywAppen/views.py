from django.shortcuts import render
from mhywApp.models import *
# Create your views here.
def landingen(request):
    
    duyuru=Duyuru.objects.all().order_by("-id")
    context={
        "duyurular":duyuru
    }
    return render(request,"landingen.html",context)
def derinmevzuen(request):
    return render(request,"derinmevzuen.html")
def hakkimizdaen(request):
    return render(request,"hakkimizdaen.html")
def iletisimen(request):
    return render(request,"iletisimen.html")
def mentalhealth101en(request):
    return render(request,"mentalhealth101en.html")
def stigmaen(request):
    return render(request,"stigmaen.html")

def duyuren(request, duyuruId):
    duyurular=Duyuru.objects.filter(basliken = duyuruId)
    context={
        'duyurular':duyurular
    }
    return render(request,"duyuruen.html",context)