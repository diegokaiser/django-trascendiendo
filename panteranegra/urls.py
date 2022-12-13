"""panteranegra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lobogris import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('workarea/', views.workarea, name='workarea'),
    path('workarea/signup/', views.signup, name='signin'),
    path('workarea/login/', views.signin, name='login'),
    path('workarea/logout/', views.signout, name='logout'),

    path('workarea/tasks/', views.tasks, name='workarea/tasks'),
    path('workarea/tasks/create/', views.tasks_create,
         name='workarea/tasks/create'),
    path('workarea/tasks/detail/<int:task_id>/', views.tasks_detail,
         name='workarea/tasks/detail'),
    path('workarea/tasks/edit/<int:task_id>/', views.tasks_edit,
         name='workarea/tasks/edit'),

    path('workarea/projects/', views.projects, name='workarea/projects'),
    path('workarea/projects/create/', views.projects_create,
         name='workarea/projects/create'),
    path('workarea/projects/detail/<int:project_id>/', views.projects_detail,
         name='workarea/projects/detail'),
    path('workarea/projects/edit/<int:project_id>/', views.projects_edit,
         name='workarea/projects/edit'),

    path('workarea/finances/incomings/', views.finances_incomings,
         name='workarea/finances/incomings'),
    path('workarea/finances/incomings/create/', views.finances_incomings_create,
         name='workarea/finances/incomings/create'),
    path('workarea/finances/incomings/detail/<int:incoming_id>/', views.finances_incomings_detail,
         name='workarea/finances/incomings/detail'),
    path('workarea/finances/incomings/edit/<int:incoming_id>/', views.finances_incomings_edit,
         name='workarea/finances/incomings/edit'),

    path('workarea/finances/outgoings/', views.finances_outgoings,
         name='workarea/finances/outgoings'),
    path('workarea/finances/outgoings/create/', views.finances_outgoings_create,
         name='workarea/finances/outgoings/create'),
    path('workarea/finances/outgoings/detail/<int:outgoing_id>/', views.finances_outgoings_detail,
         name='workarea/finances/outgoings/detail'),
    path('workarea/finances/outgoings/edit/<int:outgoing_id>/', views.finances_outgoings_edit,
         name='workarea/finances/outgoings/edit'),

    path('workarea/contacts/', views.contacts, name='workarea/contacts'),
    path('workarea/contacts/create/', views.contacts,
         name='workarea/contacts/create'),
    path('workarea/contacts/detail/<int:contact_id>/', views.contacts_detail,
         name='workarea/contacts/detail'),
    path('workarea/contacts/edit/<int:contact_id>/', views.contacts_edit,
         name='workarea/contacts/edit'),

    path('workarea/datum/', views.datum, name='workarea/datum'),
    path('workarea/datum/detail/<int:datum_id>/', views.datum_detail,
         name='workarea/datum/detail'),
    path('workarea/datum/edit/<int:datum_id>/', views.datum_edit,
         name='workarea/datum/edit'),
]
