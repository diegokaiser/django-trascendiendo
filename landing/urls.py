from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.userlogin, name='login'),
    path('lists/', views.lists, name='lists')
]
