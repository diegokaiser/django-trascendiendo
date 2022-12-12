from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskCreate, ContactCreate, IncomingCreate, OutgoingCreate, ProjectCreate
from .models import Task, Contact, Incoming, Outgoing, Project

# Create your views here.

# home


def home(request):
    if request.method == 'GET':
        return render(request, 'index.html', {
            'form': ContactCreate
        })
    else:
        try:
            form = ContactCreate(request.POST)
            new_contact = form.save(commit=False)
            new_contact.save()
            return redirect('home')
        except ValueError:
            return render(request, 'index.html', {
                'form': ContactCreate,
                'error': 'Por favor, provee datos válidos'
            })

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
    projects = Project.objects.all()
    return render(request, 'workarea/projects/index.html', {
        'projects': projects
    })


def projects_create(request):
    if request.method == 'GET':
        return render(request, 'workarea/projects/create.html', {
            'form': ProjectCreate
        })
    else:
        try:
            form = ProjectCreate(request.POST)
            new_project = form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            return redirect('workarea/projects')
        except ValueError:
            return render(request, 'workarea/projects/create.html', {
                'form': ProjectCreate,
                'error': 'Por favor, provee datos válidos'
            })


# finances/incomings
def finances_incomings(request):
    incomings = Incoming.objects.all()
    return render(request, 'workarea/finances/incomings/index.html', {
        'incomings': incomings
    })


def finances_incomings_create(request):
    if request.method == 'GET':
        return render(request, 'workarea/finances/incomings/create.html', {
            'form': IncomingCreate
        })
    else:
        try:
            form = IncomingCreate(request.POST)
            new_incoming = form.save(commit=False)
            new_incoming.user = request.user
            new_incoming.save()
            return redirect('workarea/finances/incomings')
        except ValueError:
            return render(request, 'workarea/finances/incomings/create.html', {
                'form': IncomingCreate,
                'error': 'Por favor, provee datos válidos'
            })


# finances/outgoings
def finances_outgoings(request):
    outgoings = Outgoing.objects.all()
    return render(request, 'workarea/finances/outgoings/index.html', {
        'outgoings': outgoings
    })


def finances_outgoings_create(request):
    if request.method == 'GET':
        return render(request, 'workarea/finances/outgoings/create.html', {
            'form': OutgoingCreate
        })
    else:
        try:
            form = OutgoingCreate(request.POST)
            new_outgoing = form.save(commit=False)
            new_outgoing.user = request.user
            new_outgoing.save()
            return redirect('workarea/finances/outgoings')
        except ValueError:
            return render(request, 'workarea/finances/outgoings/create.html', {
                'form': OutgoingCreate,
                'error': 'Por favor, provee datos válidos'
            })


# contacts
def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'workarea/contacts/index.html', {
        'contacts': contacts
    })


def contacts_create(request):
    if request.method == 'GET':
        return render(request, 'workarea/contacts/create.html', {
            'form': ContactCreate
        })
    else:
        try:
            form = ContactCreate(request.POST)
            new_contact = form.save(commit=False)
            new_contact.save()
            return redirect('workarea/contacts')
        except ValueError:
            return render(request, 'workarea/contacts/create.html', {
                'form': ContactCreate,
                'error': 'Por favor, provee datos válidos'
            })


# datum
def datum(request):
    return render(request, 'workarea/datum/index.html')


def datum_create(request):
    return render(request, 'workarea/datum/create.html')
