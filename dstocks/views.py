"""from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


@login_required     
def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    return render(request,"contact.html")

def error(request):
    return render(request,"error.html")

def single(request):
    return render(request,"single.html")

def projects(request):
    return render(request,"projects.html")

def register(request):
    return render(request,"register.html")

def register_c(request):
    if request.method == 'POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, 'fack account is created for {username}')
            return redirect('user_login')
        else:
            form = UserRegisterForm()
        return render(request,'register.html',{'form':form})

def login_c(request):
    contex = {}
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('user_sucess'))
        else:
            contact["Error"]
            return render(render,"indexl.html",contact)
    else:
        return render(request,"indexl.html",contact)
        
def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home/")
        else:
            massages.info(request,'Invalid')
            return redirect('indexl')
    else:
        return render(request,"indexl.html")
"""