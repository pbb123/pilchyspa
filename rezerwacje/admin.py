from django.contrib import admin
from .models import Rodzina,Pokoj,Rezerwacja,Error,Day

admin.site.register(Rodzina)
admin.site.register(Rezerwacja)
admin.site.register(Pokoj)
admin.site.register(Error)
admin.site.register(Day)
