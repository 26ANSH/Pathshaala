from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/login/', views.User_Login, name='login'),
    path('auth/logout/', views.my_logout, name='logout'),
    path('auth/signup/', views.signin, name='signup'),
    path('auth/verify/', views.verifyemail, name='verify'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/courses/<slug:course_id>/students/', views.students, name="students"),
    path('dashboard/courses/', views.courses, name="courses"),
    path('dashboard/resources/', views.sr, name="smart resources"),
    path('dashboard/videos/', views.sv, name="smart videos"),
    path('dashboard/courses/create/', views.new_course, name="new_course"),
    path('dashboard/courses/<slug:course_id>', views.course, name="course"),
    path('dashboard/courses/<slug:course_id>/docs', views.docs, name="docs"),
]