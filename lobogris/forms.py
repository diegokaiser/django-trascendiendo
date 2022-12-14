from django import forms
from django.forms import ModelForm
from .models import Task, Contact, Incoming, Outgoing, Project


class TaskCreate(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority']
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'priority': 'Prioridad'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'type': 'date'}),
            'priority': forms.TextInput(attrs={'class': 'form-control'}),
        }


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


class IncomingCreate(ModelForm):
    class Meta:
        model = Incoming
        fields = ['amount', 'description']
        labels = {
            'amount': 'Monto',
            'description': 'Descripción'
        }
        widgets = {
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'type': 'date'}),
        }


class OutgoingCreate(ModelForm):
    class Meta:
        model = Outgoing
        fields = ['amount', 'description']
        labels = {
            'amount': 'Monto',
            'description': 'Descripción'
        }
        widgets = {
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'type': 'date'}),
        }


class ProjectCreate(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'code', 'description', 'due_at',
                  'type_of_incoming', 'budget', 'contact']
        labels = {
            'title': 'Nombre',
            'code': 'Código',
            'description': 'Descripción',
            'due_at': 'Fecha límite',
            'type_of_incoming': 'Tipo de ingreso',
            'budget': 'Presupuesto',
            'contact': 'Cliente'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'due_at': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'type_of_incoming': forms.TextInput(attrs={'class': 'form-control'}),
            'budget': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.Select(attrs={'class': 'form-control'})
        }
