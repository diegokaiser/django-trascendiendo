from django.contrib import admin
from .models import Task, Contact, Incomming, Outgoing, Company

# Register your models here.
admin.site.register(Company)
admin.site.register(Outgoing)
admin.site.register(Incomming)
admin.site.register(Contact)
admin.site.register(Task)