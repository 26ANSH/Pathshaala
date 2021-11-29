from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_student, name='index_student'),
    path('auth/verify/', views.student, name='verify'),
    path('auth/login/', views.login_student, name='login'),
    path('auth/logout/', views.logout_student, name='logout')
]