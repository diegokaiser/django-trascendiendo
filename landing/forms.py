from django import forms
from .models import Contact


class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nombre', 'telefono', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input__field input__field--haruki', 'required': ''}),
            'telefono': forms.TextInput(attrs={'class': 'input__field input__field--haruki', 'required': '', 'pattern': '/^\d+$/;'}),
            'email': forms.TextInput(attrs={'class': 'input__field input__field--haruki', 'required': '', 'pattern': '[a-z0-9]+@[a-z]+\.[a-z]{2,3}'}),
        }
