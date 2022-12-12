from django.contrib import admin
from .models import Task, Contact, Incoming, Outgoing, Project


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "deleted_at")


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "deleted_at")


class IncomingAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


class OutgoingAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Incoming, IncomingAdmin)
admin.site.register(Outgoing, OutgoingAdmin)
admin.site.register(Project, ProjectAdmin)
