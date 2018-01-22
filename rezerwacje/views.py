from django.shortcuts import render,redirect,get_object_or_404
from .models import Rodzina,Rezerwacja,Pokoj,Error,Day
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as l
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('menu')
    if request.method=="POST":
        user=request.POST['user']
        password=request.POST['pass']
        user=authenticate(username=user,password=password)
        if user is not None:
            l(request, user)
            return redirect('menu')
        else:
            return render(request,'rezerwacje/index.html',{'e':True})
    else:
        return render(request,'rezerwacje/index.html',{'e':False})

def new(request):
    if request.user.is_authenticated:
        days=Day.objects.filter().order_by('numer')
        rezerwacje=Rezerwacja.objects.all()
        pokoje=Pokoj.objects.all()
        family=get_object_or_404(Rodzina,user=request.user)
        if request.method=="POST":
            od=int(request.POST['od'])
            do=int(request.POST['do'])
            if od<do:
                rezerwacje=rezerwacje.exclude(od__lt=od,do__lt=od)
                rezerwacje=rezerwacje.exclude(od__gt=do,do__gt=do)
                for rez in rezerwacje:
                    pokoj=rez.pokoj
                    pokoje=pokoje.exclude(pk=pokoj.pk)
                return render(request,'rezerwacje/rooms.html',{'pokoje':pokoje,'od':od,'do':do})
            else:
                #od<do
                return render(request,'rezerwacje/new.html',{'family':family,'e':True,'days':days,'a':(od,do)})
        else:#get
            return render(request,'rezerwacje/new.html',{'family':family,'days':days})
    else:#niezalogowany
        return redirect('login')
def rezerwacja(request,od,do,pok):
    if request.user.is_authenticated:
        rezerwacje=Rezerwacja.objects.all()
        pokoje=Pokoj.objects.all()
        if request.method=="GET":
            #metoda GET
            pokoj=get_object_or_404(Pokoj,maphref="/"+pok)
            pokojid=pokoj.id
            rezerwacje=Rezerwacja.objects.all()
            rezerwacje=rezerwacje.exclude(od__lt=od,do__lt=od)
            rezerwacje=rezerwacje.exclude(od__gt=do,do__gt=do)
            rezerwacje=rezerwacje.filter(pokoj__id=pokojid)
            rezerwacje_rodziny=Rezerwacja.objects.filter(rodzina=get_object_or_404(Rodzina,user=request.user))
            zarezerwowane_miejsca=0
            komunikat=False
            for rez in rezerwacje_rodziny:
                zarezerwowane_miejsca+=rez.pokoj.rozmiar
            pozostałe_osoby=get_object_or_404(Rodzina,user=request.user).liczebność-zarezerwowane_miejsca
            if len(rezerwacje)==0:
                pokoj=Pokoj.objects.get(id=pokojid)
                rodzina=Rodzina.objects.get(user=request.user)
                nowa=Rezerwacja.objects.create(rodzina=rodzina,pokoj=pokoj,od=od,do=do,rozmiar=pokoj.rozmiar)
                nowa.save()
                komunikat=True
                return redirect('ludzie',nowa.id)
            else:
                komunikat=False
                return render(request,'rezerwacje/koniec_rezerwacji.html',{'komunikat':komunikat,'z_m':pozostałe_osoby})
    else:
        #Nie zalogowany
        return redirect('login')

def see(request):
    if request.user.is_authenticated:
        rez=Rezerwacja.objects.all()
        return render(request,'rezerwacje/see.html',{'rezerwacje':rez,'u':request.user})
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
def menu(request):
    if request.user.is_authenticated:
        return render(request,'rezerwacje/zalogowany.html',{'user':request.user})
    else:
        return redirect('login')
def changepass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            old=request.POST['starehaslo']
            new1=request.POST['nowehaslo']
            new2=request.POST['nowehaslo2']
            oldc=authenticate(username=request.user.username,password=old)
            if oldc and new1==new2:
                oldc.set_password(new1)
                oldc.save()
                logout(request)
                return render(request,'rezerwacje/changepassyes.html',{})
            else:
                return render(request,'rezerwacje/changepass.html',{'e':True})
        else:
            return render(request,'rezerwacje/changepass.html',{'e':False})
    else:
        return redirect('login')
def adderror(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            rodzina=get_object_or_404(Rodzina,user=request.user)
            opis=request.POST['opis']
            nowy=Error.objects.create(opis=opis,rodzina=rodzina)
            nowy.save()
            return render(request,'rezerwacje/errors2.html',{})
        else:
            return render(request,'rezerwacje/errors.html',{})
    else:
        return redirect('login')
def delete(request,id):
    if request.user.is_authenticated:
        rez=get_object_or_404(Rezerwacja,id=id)
        if rez.rodzina.user==request.user:
            rezs=Rezerwacja.objects.all()
            rezs=rezs.exclude(od__lt=rez.od,do__lt=rez.od)
            rezs=rezs.exclude(od__gt=rez.do,do__gt=rez.do)
            rez.delete()
            for rezerwacja in rezs:
                for dayx in range(rezerwacja.od,rezerwacja.do+1):
                    day=get_object_or_404(Day,numer=dayx)
                    suma=0
                    rezerwacje=Rezerwacja.objects.all()
                    rezerwacje=rezerwacje.exclude(od__lt=dayx,do__lt=dayx)
                    rezerwacje=rezerwacje.exclude(od__gt=dayx,do__gt=dayx)
                    for rez in rezerwacje:
                        suma+=rez.rozmiar
                    if suma<day.limit:
                        rezerwacja.limit=False
                        rezerwacja.save()

        return redirect('see')
    else:
        return redirect('login')
def autor(request):
    return render(request,'rezerwacje/autor.html',{})
def ludzie(request,pk):
    if request.user.is_authenticated:
        rezerwacja=get_object_or_404(Rezerwacja,id=pk)
        if not rezerwacja.rodzina.user==request.user:
            return redirect("/")
        if request.method=="POST":
            rozmiar=request.POST['x']
            if not rozmiar:
                return render(request,'rezerwacje/people.html',{'e':True})
            rezerwacja.rozmiar=rozmiar
            rezerwacja.save()
            flag=False
            for dayx in range(rezerwacja.od,rezerwacja.do+1):
                day=get_object_or_404(Day,numer=dayx)
                suma=0
                rezerwacje=Rezerwacja.objects.all()
                rezerwacje=rezerwacje.exclude(od__lt=dayx,do__lt=dayx)
                rezerwacje=rezerwacje.exclude(od__gt=dayx,do__gt=dayx)
                for rez in rezerwacje:
                    suma+=rez.rozmiar
                if suma>day.limit:
                    flag=True
                    rezerwacja.limit=True
                    rezerwacja.save()
                    return redirect('limit',pk=pk)

            return render(request,'rezerwacje/koniec_rezerwacji.html',{'komunikat':True})
        else:
            return render(request,'rezerwacje/people.html',{'e':False})
            #get
    else:
        return redirect('login')
def limit(request,pk):
    if request.user.is_authenticated:
        rezerwacja=get_object_or_404(Rezerwacja,id=pk)
        if not rezerwacja.rodzina.user==request.user:
            return redirect("/")
        if request.method=="POST":
            wynik=request.POST['h']
            if wynik=="uny":
                return render(request,'rezerwacje/koniec_rezerwacji.html',{'komunikat':True})
            elif wynik=="duy":
                return redirect('del',id=pk)
            return render(request,"rezerwacje/limit.html",{'a':wynik})
        else:
            return render(request,"rezerwacje/limit.html",{})

    else:
        return redirect('login')
