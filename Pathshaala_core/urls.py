from django.contrib import admin
from django.urls import path, include

from . import front 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', front.index, name='index'),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
]