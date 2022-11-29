from django.db import models

# Create your models here.


class Contact(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
