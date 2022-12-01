from django.shortcuts import render
from mhywApp.models import *
# Create your views here.
def landingar(request):
    
    duyuru=Duyuru.objects.all().order_by("-id")
    context={
        "duyurular":duyuru
    }
    return render(request,"landingar.html",context)
def derinmevzuar(request):
    return render(request,"derinmevzuar.html")
def hakkimizdaar(request):
    return render(request,"hakkimizdaar.html")
def iletisimar(request):
    return render(request,"iletisimar.html")
def mentalhealth101ar(request):
    return render(request,"mentalhealth101ar.html")
def stigmaar(request):
    return render(request,"stigmaar.html")
def duyurar(request, duyuruId):
    duyurular=Duyuru.objects.filter(baslikar = duyuruId)
    context={
        'duyurular':duyurular
    }
    return render(request,"duyuruar.html",context)