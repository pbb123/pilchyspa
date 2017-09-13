from django.shortcuts import render,redirect,get_object_or_404
from .models import Rodzina,Rezerwacja,Pokoj
from django.contrib.auth import authenticate
from django.contrib.auth import login as l
# Create your views here.
def login(request):
    if request.method=="POST":
        user=request.POST['user']
        password=request.POST['pass']
        user=authenticate(username=user,password=password)
        if user is not None:
            l(request, user)
            return render(request,'rezerwacje/zalogowany.html',{'user':request.user})
        else:
            return render(request,'rezerwacje/index.html',{})
    else:
        return render(request,'rezerwacje/index.html',{})

def new(request):
    if request.user.is_authenticated:
        family=get_object_or_404(Rodzina,user=request.user)
        if request.method=="POST":
            od=int(request.POST['od'])
            do=int(request.POST['do'])
            rezerwacje=Rezerwacja.objects.all()
            pokoje=Pokoj.objects.all()
            if od<=do:
                rezerwacje=rezerwacje.exclude(od__lt=od,do__lt=od)
                rezerwacje=rezerwacje.exclude(od__gt=do,do__gt=do)
                for rez in rezerwacje:
                    pokoj=rez.pokoj
                    pokoje=pokoje.exclude(pk=pokoj.pk)
                return render(request,'rezerwacje/rooms.html',{'family':family,'pokoje':pokoje})
            #Zły termin: od>do
            return render(request,'rezerwacje/rooms.html',{'family':family,'komunikat':'nie'})
        else:
            return render(request,'rezerwacje/new.html',{'family':family})
    else:
        return redirect('login')

    
    
