from django.urls import path
from . import views

urlpatterns = [
    path('', views.basic, name='basic'),
    path('student/', views.index, name='index'),
]