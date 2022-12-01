"""MHYW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mhywApp.views import *
from mhywAppar.views import *
from mhywAppen.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landing, name='anasayfa'),
    path('duyuru/<str:duyuruId>',duyurr,name='duyuru'),
    path('İletişim',iletisim,name='iletisim'),
    path('Hakkımızda',hakkimizda,name='hakkimizda'),
    path('stigma',stigma,name="stigma"),
    path('derinmevzu',derinMevzu,name="derinmevzu"),
    path('mentalhealth101',mentalhealth101,name="mentalhealth"),
    path('en',landingen,name="landingen"),
    path('en/about-us',hakkimizdaen,name="hakkimizdaen"),
    path('en/news/<str:duyuruId>',duyuren,name='duyuruen'),
    path('en/deepissue',derinmevzuen,name="derinmevzuen"),
    path('en/mentalhealth101',mentalhealth101en,name="mentalhealth101en"),
    path('en/contact',iletisimen,name="iletisimen"),
    path('en/stigma',stigmaen,name="stigmaen"),
    path('ar',landingar,name="landingar"),
    path('ar/news/<str:duyuruId>',duyurar,name='duyuruar'),
    path('ar/about-usar',hakkimizdaar,name="hakkimizdaar"),
    path('ar/deepissuear',derinmevzuar,name="derinmevzuar"),
    path('ar/mentalhealth101ar',mentalhealth101ar,name="mentalhealth101ar"),
    path('ar/contactar',iletisimar,name="iletisimar"),
    path('ar/stigmaar',stigmaar,name="stigmaar"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#+static: dosya ekleme komudu iki kutuphane eklenmesi lazim
