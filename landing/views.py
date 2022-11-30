from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .forms import CreateContactForm
from .models import Contact
from django.utils import timezone

# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {
            'form': CreateContactForm
        })
    else:
        try:
            form = CreateContactForm(request.POST)
            new_contact = form.save(commit=False)
            new_contact.save()
        except:
            return render(request, 'index.html', {
                'form': CreateContactForm,
                'error': 'El mensaje no ha sido enviado'
            })


@login_required
def userlogout(request):
    logout(request)
    return redirect('admin')


def userlogin(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos.'
            })
        else:
            login(request, user)
            return redirect('lists')


@login_required
def lists(request):
    lists = Contact.objects.filter(created_at__isnull=False)
    return render(request, 'lists.html', {
        'lists': lists
    })
