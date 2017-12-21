from django.db import models
from django.contrib.auth.models import User

class Rodzina(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    liczebność=models.IntegerField()
    def __str__(self):
        return str(self.user)
class Pokoj(models.Model):
    rozmiar=models.IntegerField()
    nazwa=models.TextField()
    maphref=models.TextField()
    mapshape=models.TextField()
    mapcoords=models.TextField()
    def __str__(self):
         return self.nazwa
class Rezerwacja(models.Model):
     od=models.IntegerField()
     do=models.IntegerField()
     pokoj=models.ForeignKey(Pokoj,on_delete=models.CASCADE)
     rodzina=models.ForeignKey(Rodzina,on_delete=models.CASCADE)
     rozmiar=models.IntegerField(null=True)
     limit=models.NullBooleanField()
     def __str__(self):
         return "Od: "+str(self.od)+" Do: "+str(self.do)+" Przez: "+str(self.rodzina)+" W pokoju: "+str(self.pokoj)
    
class Error(models.Model):
    rodzina=models.ForeignKey(Rodzina,on_delete=models.CASCADE)
    opis=models.TextField()
    
class Day(models.Model):
    numer=models.IntegerField()
    limit=models.IntegerField()
    nazwa=models.TextField()
    def __str__(self):
        return str(self.nazwa)+"("+str(self.limit)+")"
