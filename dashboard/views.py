from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request,'base.html')
def erropage(request):
    return render(request,'erro.html')
def okpage(request):
    return render(request,'ok.html')
def registerpage(request):
    if request.method=="POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        email1 = request.POST.get('email1')
        email2 = request.POST.get('email2')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if email1==email2:
            if password1==password2:
                if User.objects.filter(username=username).exists() == False:
                    user = User.objects.create_user(username=username, email=email1,
                                     password=password1)
                    return redirect('home')
                else:
                    messages.add_message(request, messages.ERROR,"Usuário já existe")
                    return render(request, 'cadastro.html')
            else:
                messages.add_message(request, messages.ERROR,"Password invalido")
                return render(request, 'cadastro.html')
        else:
            messages.add_message(request, messages.ERROR,"Email invalido")
            return render(request, 'cadastro.html')
        return render(request, 'cadastro.html')
    else:
        return render(request, 'cadastro.html')
def loginpage(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR,"Credenciais inválidas")
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def userlogout(request):
    logout(request)
    return redirect('home')

@login_required
def userpage(request):
    return render(request, 'dashboard.html')
