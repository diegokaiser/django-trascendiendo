from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskCreate
from .models import Task

# Create your views here.

# home


def home(request):
    return render(request, "index.html")

# workarea


def workarea(request):
    return render(request, 'workarea/index.html')

# register


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

# login


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

# logout


def signout(request):
    logout(request)
    return redirect('login')


# workarea functions
# tasks
def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'workarea/tasks/index.html', {
        'tasks': tasks
    })


def tasks_create(request):
    if request.method == 'GET':
        return render(request, 'workarea/tasks/create.html', {
            'form': TaskCreate
        })
    else:
        try:
            form = TaskCreate(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('workarea/tasks')
        except ValueError:
            return render(request, 'workarea/tasks/create.html', {
                'form': TaskCreate,
                'error': 'Por favor, provee datos válidos'
            })


# projects
def projects(request):
    return render(request, 'workarea/projects/index.html')


# finances/incomings
def finances_incomings(request):
    return render(request, 'workarea/finances/index.html')


# finances/outgoings
def finances_outgoings(request):
    return render(request, 'workarea/finances/index.html')


# contacts
def contacts(request):
    return render(request, 'workarea/contacts/index.html')


# datum
def datum(request):
    return render(request, 'workarea/datum/index.html')
