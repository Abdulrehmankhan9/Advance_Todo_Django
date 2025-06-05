from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # default/home page of todo
]
