from django.contrib import admin
from .models import Task, Contact


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "deleted_at")


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "deleted_at")


# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(Contact, ContactAdmin)
