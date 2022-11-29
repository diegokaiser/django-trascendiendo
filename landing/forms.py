from django.forms import ModelForm
from .models import Contact


class CreateContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['nombre', 'telefono', 'email']
