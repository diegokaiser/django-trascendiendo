from django import forms
from django.forms import ModelForm
from .models import Task, Contact


class TaskCreate(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority']


class ContactCreate(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'lastname', 'email']
        labels = {
            'name': 'Nombre',
            'lastname': 'Apellidos',
            'email': 'Correo electrónico'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input__field input__field--haruki field__name', 'required': '', "autocomplete": "nope"}),
            'lastname': forms.TextInput(attrs={'class': 'input__field input__field--haruki field__lastname', 'required': '', "autocomplete": "nope"}),
            'email': forms.TextInput(attrs={'class': 'input__field input__field--haruki field__email', 'required': '', "autocomplete": "nope"}),
        }
