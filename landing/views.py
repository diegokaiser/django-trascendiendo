from django.shortcuts import render
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
        return render(request, 'index.html', {
            'form': CreateContactForm
        })
