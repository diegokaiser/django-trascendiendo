from django import forms
from .models import Contact


class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nombre', 'telefono', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input__field input__field--haruki', 'required': '', "autocomplete": "nope"}),
            'telefono': forms.TextInput(attrs={'class': 'input__field input__field--haruki field__phone', 'required': '', "autocomplete": "nope"}),
            'email': forms.TextInput(attrs={'class': 'input__field input__field--haruki field__email', 'required': '', "autocomplete": "nope"}),
        }
