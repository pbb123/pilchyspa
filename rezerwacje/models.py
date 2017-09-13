from django.db import models
from django.contrib.auth.models import User

class Rodzina(models.Model):
    user=models.ForeignKey(User)
    liczebność=models.IntegerField()
class Pokoj(models.Model):
    rozmiar=models.IntegerField()
    nazwa=models.TextField()
class Rezerwacja(models.Model):
     od=models.IntegerField()
     do=models.IntegerField()
     pokoj=models.ForeignKey(Pokoj)
     rodzina=models.ForeignKey(Rodzina)
     def __str__(self):
         return "Od: "+str(self.od)+" Do: "+str(self.do)
    
