from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/login/', views.User_Login, name='login'),
    path('auth/logout/', views.my_logout, name='logout'),
    path('auth/signup/', views.signin, name='signup'),
    #  path('auth/verifyemail/', views.verifyemail, name='verifyemail'),
    path('dashboard/', views.securepage, name="dashboard")
]