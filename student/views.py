from django.http import HttpResponse
from django.shortcuts import render

import random
# login authenticate module in django.contrib

def is_teacher(request):
    if request.user.username.split('_')[0]=='teacher':
        return True
    else:
        return False

def student_auth(request):
    if request.user.is_authenticated and request.user.username.split('_')[0]=='student':
        return True
    else:
        return False

def index(request):
    if student_auth(request):
        return render(request, 'student/say.html', {'say': f' Pathshaala ❤️ {request.user.first_name}'})
    elif is_teacher(request):
        return HttpResponse('Logged in as Teacher')
    else:
        return HttpResponse('Login to Access !!!')