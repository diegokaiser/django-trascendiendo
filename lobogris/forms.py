from django.forms import ModelForm
from .models import Task, Contact


class TaskCreate(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority']


class ContactCreate(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'lastname', 'email', 'phone', 'company']
