from django.shortcuts import render,redirect,get_object_or_404
from .models import Rodzina,Rezerwacja,Pokoj
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as l
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return render(request,'rezerwacje/zalogowany.html',{'user':request.user})
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
            od=request.POST['od']
            do=request.POST['do']
            return redirect('rooms',od=od,do=do)  
        else:
            return render(request,'rezerwacje/new.html',{'family':family})
    else:
        return redirect('login')
def rooms(request,od,do):
    if request.user.is_authenticated:
        rezerwacje=Rezerwacja.objects.all()
        pokoje=Pokoj.objects.all()
        if request.method=="GET":
            if od<do:
                rezerwacje=rezerwacje.exclude(od__lt=od,do__lt=od)
                rezerwacje=rezerwacje.exclude(od__gt=do,do__gt=do)
                for rez in rezerwacje:
                    pokoj=rez.pokoj
                    pokoje=pokoje.exclude(pk=pokoj.pk)
                return render(request,'rezerwacje/rooms.html',{'pokoje':pokoje})
            else:
                #od<do
                return redirect('new')

        else:
            #metoda POST
            pokojid=request.POST['pokoje']
            rezerwacje=Rezerwacja.objects.all()
            rezerwacje=rezerwacje.exclude(od__lt=od,do__lt=od)
            rezerwacje=rezerwacje.exclude(od__gt=do,do__gt=do)
            rezerwacje=rezerwacje.filter(pokoj__id=pokojid)
            if len(rezerwacje)==0:
                pokoj=Pokoj.objects.get(id=pokojid)
                rodzina=Rodzina.objects.get(user=request.user)
                nowa=Rezerwacja.objects.create(rodzina=rodzina,pokoj=pokoj,od=od,do=do)
                nowa.save()
                komunikat=True
            else:
                komunikat=False
            return render(request,'rezerwacje/koniec_rezerwacji.html',{'komunikat':komunikat})
    else:
        #Nie zalogowany
        return redirect('login')

def see(request):
    if request.user.is_authenticated:
        rez=Rezerwacja.objects.all()
        return render(request,'rezerwacje/see.html',{'rezerwacje':rez})
    else:
        return redirect('login')
def setings(request):
    if request.user.is_authenticated:
        return render(request,'rezerwacje/set.html',{})
    else:
        return redirect('login')
def logoutview(request):
    logout(request)
    return redirect('login')

    
    
