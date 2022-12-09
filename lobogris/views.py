from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.


def home(request):
    return render(request, "index.html")


def workarea(request):
    return render(request, 'workarea/index.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'workarea/signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('workarea')
            except IntegrityError:
                return render(request, 'workarea/signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'workarea/signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })


def signin(request):
    if request.method == 'GET':
        return render(request, 'workarea/login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'workarea/login.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o contraseña no son correctos'
            })
        else:
            login(request, user)
            return redirect('workarea')


def signout(request):
    logout(request)
    return redirect('login')
