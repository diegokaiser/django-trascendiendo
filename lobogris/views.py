from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(request):
  return render(request, 'index.html')

def workarea(request):
  if request.method == 'GET':
    #TODO si existe sesion
    return render(request, 'workarea/index.html')
  else:
    return redirect('login')

def createuser(request):
  if request.method == 'GET':
    return render(request, 'signup.html', {
      'form': UserCreationForm
    })
  else:
    if request.POST['password1'] == request.POST['password2']:
      try:
        user = User.objects.create_user(
          username = request.POST['username'],
          password = request.POST['password1']
        )
        user.save()
        return render(request, 'index.html')
      except:
        return render(request, 'signup.html', {
          'form': UserCreationForm,
          'error': 'El usuario ya existe'
        })
    return render(request, 'signup.html', {
      'form': UserCreationForm,
      'error': 'Las contraseñas no coinciden'
    })

def signout(request):
  logout(request)
  return redirect('home')

def signin(request):
  if request.method == 'GET':
    return render(request, 'workarea/index.html', {
      'form': AuthenticationForm
    })
  else:
    user = authenticate(
      request,
      username=request.POST['username'],
      password=request.POST['password']
    )
    if user is None:
      return render(request, 'workarea/index.html', {
        'form': AuthenticationForm,
        'error': 'Usuario o contraseña incorrectos'
      })
    else:
      login(request, user)
      return redirect('tasks')

def tasks(request):
  return render(request, 'workarea/index.html')
