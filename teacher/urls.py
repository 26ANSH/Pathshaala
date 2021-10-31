from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.User_Login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('signup/', views.signin, name='signup'),
]