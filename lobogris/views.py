from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
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
@login_required
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
@login_required
def signout(request):
    logout(request)
    return redirect('login')


# workarea functions
# tasks
@login_required
def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'workarea/tasks/index.html', {
        'tasks': tasks
    })


@login_required
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


@login_required
def tasks_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'workarea/tasks/detail.html', {
        'task': task
    })


@login_required
def tasks_edit(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id)
        form = TaskCreate(instance=task)
        return render(request, 'workarea/tasks/edit.html', {
            'task': task,
            'form': form
        })
    else:
        try:
            task = get_object_or_404(Task, pk=task_id)
            form = TaskCreate(request.POST, instance=task)
            form.save()
            return render(request, 'workarea/tasks/detail.html', {
                'task': task
            })
        except ValueError:
            return render(request, 'workarea/tasks/edit.html', {
                'task': task,
                'form': form,
                'error': 'Error al actualizar'
            })


# projects
@login_required
def projects(request):
    projects = Project.objects.all()
    return render(request, 'workarea/projects/index.html', {
        'projects': projects
    })


@login_required
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


@login_required
def projects_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'workarea/projects/detail.html', {
        'project': project
    })


@login_required
def projects_edit(request, project_id):
    project = get_object_or_404(Project, k=project_id)
    return render(request, 'workarea/projects/edit.html', {
        'project': project
    })


# finances/incomings
@login_required
def finances_incomings(request):
    incomings = Incoming.objects.all()
    return render(request, 'workarea/finances/incomings/index.html', {
        'incomings': incomings
    })


@login_required
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


@login_required
def finances_incomings_detail(request, incoming_id):
    incoming = get_object_or_404(Incoming, pk=incoming_id)
    return render(request, 'workarea/finances/incomings/detail.html', {
        'incoming': incoming
    })


@login_required
def finances_incomings_edit(request, incoming_id):
    incoming = get_object_or_404(Incoming, pk=incoming_id)
    return render(request, 'workarea/finances/incomings/edit.html', {
        'incoming': incoming
    })


# finances/outgoings
@login_required
def finances_outgoings(request):
    outgoings = Outgoing.objects.all()
    return render(request, 'workarea/finances/outgoings/index.html', {
        'outgoings': outgoings
    })


@login_required
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


@login_required
def finances_outgoings_detail(request, outgoing_id):
    outgoing = get_object_or_404(Outgoing, pk=outgoing_id)
    return render(request, 'workarea/finances/outgoings/detail.html', {
        'outgoing': outgoing
    })


@login_required
def finances_outgoings_edit(request, outgoing_id):
    outgoing = get_object_or_404(Outgoing, pk=outgoing_id)
    return render(request, 'workarea/finances/outgoings/edit.html', {
        'outgoing': outgoing
    })


# contacts
@login_required
def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'workarea/contacts/index.html', {
        'contacts': contacts
    })


@login_required
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


@login_required
def contacts_detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'workarea/contacts/detail.html', {
        'contact': contact
    })


@login_required
def contacts_edit(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'workarea/contacts/edit.html', {
        'contact': contact
    })


# datum
@login_required
def datum(request):
    return render(request, 'workarea/datum/index.html')


@login_required
def datum_create(request):
    if request.method == 'GET':
        return render(request, 'workarea/datum/create.html')
    else:
        return render(request, 'workarea/datum/create.html')


@login_required
def datum_edit(request, datum_id):
    return render(request, 'workarea/datum/edit.html')


@login_required
def datum_detail(request, datum_id):
    return render(request, 'workarea/datum/detail.html')
