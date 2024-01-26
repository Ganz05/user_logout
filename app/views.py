from django.shortcuts import render
from app.forms import *
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.

def register(request):
    EUFO=userForm()
    EPFO=profileForm()
    d={'EUFO':EUFO,'EPFO':EPFO}
    if request.method=='POST' and request.FILES:
        CUFO=userForm(request.POST)
        CPFO=profileForm(request.POST,request.FILES)
        if CUFO.is_valid() and CPFO.is_valid():
            MCUFO=CUFO.save(commit=False)
            pw=CUFO.cleaned_data['password']
            MCUFO.set_password(pw)
            MCUFO.save()

            MCPFO=CPFO.save(commit=False)
            MCPFO.username=MCUFO
            MCPFO.save()

            send_mail('Registration',
                      'registration is succussfull',
                      'ganesh.poojary2001@gmail.com',
                       [MCUFO.email],
                       fail_silently=True)
            return HttpResponse('Registration is Succussful')
        else:
            return HttpResponse('invalid')

    return render(request,'register.html',d)


def home(request):
    if request.session.get('username'):
        un=request.session.get('username')
        d={'un':un}
        return render(request,'home.html',d)

    return render(request,'home.html')


def userlogin(request):
    if request.method=='POST':
        un=request.POST['un']
        pw=request.POST['pw']
        AUO=authenticate(username=un,password=pw)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=un
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('invalid credentials')
    return render(request,'userlogin.html')

@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('userlogin'))

@login_required
def change_password(request):
    if request.method=='POST':
        pw=request.POST['pw']
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        UO.set_password(pw)
        UO.save()
        return HttpResponse('password changed succussfully')
    return render(request,'change_password.html')

@login_required
def view_profile(request):
    un=request.session.get('username')
    UO=User.objects.get(username=un)
    PO=profile.objects.get(username=UO)
    d={'UO':UO,'PO':PO}
    return render(request,'view_profile.html',d)





def forget_password(request):
    if request.method=='POST':
        un=request.POST['un']
        pw=request.POST['pw']
        LUO=User.objects.filter(username=un)
        if LUO:
            UO=LUO[0]
            UO.set_password(pw)
            UO.save()
            return HttpResponse('password changed succussfully')
        
    return render(request,'forget_password.html')