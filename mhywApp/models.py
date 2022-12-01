from django.db import models
from django.db import models
# Create your models here.
class Duyuru(models.Model):
    baslik=models.CharField(max_length=500,blank=True)
    basliken=models.CharField(max_length=500,null=True,blank=True)
    baslikar=models.CharField(max_length=500,null=True,blank=True)
    manset=models.TextField(max_length=500,blank=True)
    manseten=models.TextField(max_length=500,null=True,blank=True)
    mansetar=models.TextField(max_length=500,null=True,blank=True)
    kisaAciklama=models.TextField(max_length=500,null=True,blank=True)
    kisaAciklamaen=models.TextField(max_length=500,null=True,blank=True)
    kisaAciklamaar=models.TextField(max_length=500,null=True,blank=True)
    uzunAciklama=models.TextField(max_length=50000,null=True,blank=True)
    uzunAciklamaen=models.TextField(max_length=50000,null=True,blank=True)
    uzunAciklamaar=models.TextField(max_length=50000,null=True,blank=True)
    resim=models.FileField(upload_to='duyurular/',null=True,blank=True)
    baslangic=models.DateField(null=True,blank=True)
    bitis=models.DateField(null=True,blank=True)
    
    def __str__(self):
        return self.baslik

class Yazilar(models.Model):
    ad=models.CharField(max_length=500)
    yazi=models.CharField(max_length=500)
    gonderimTarihi=models.DateField(null=True,blank=True)
    kabulTarihi=models.FloatField(null=True,blank=True)
    def __str__(self):
        return self.ad
        