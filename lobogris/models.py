from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
  title           = models.CharField(max_length=200)
  description     = models.TextField(blank=True)
  created_at      = models.DateTimeField(auto_now_add=True)
  date_completed  = models.DateTimeField(null=True)
  priority        = models.BooleanField(default=False)
  user            = models.ForeignKey(User, on_delete=models.CASCADE)

class Contact(models.Model):
  name            = models.CharField(max_length=200)
  email           = models.CharField(max_length=200)
  phone           = models.CharField(max_length=200)
  contacted_yet   = models.BooleanField(null=True)
  created_at      = models.DateTimeField(auto_now_add=True)

class Incomming(models.Model):
  amount          = models.FloatField()
  curency         = models.CharField(max_length=200)
  change_currency = models.FloatField()
  description     = models.TextField(blank=True)
  created_at      = models.DateTimeField(auto_now_add=True)

class Outgoing(models.Model):
  amount          = models.FloatField()
  curency         = models.CharField(max_length=200)
  change_currency = models.FloatField()
  description     = models.TextField(blank=True)
  created_at      = models.DateTimeField(auto_now_add=True)

class Company(models.Model):
  name            = models.CharField(max_length=200)

class Project(models.Model):
  name            = models.CharField(max_length=200)
  description     = models.TextField(blank=True)
  created_at      = models.DateTimeField(auto_now_add=True)