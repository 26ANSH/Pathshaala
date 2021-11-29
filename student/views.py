from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
import asyncio
from asgiref.sync import sync_to_async
from django.core.signing import Signer
import json
import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

decode = Signer()

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

def student(request):
    if student_auth(request):
        return redirect('index')
    elif is_teacher(request):
        return HttpResponse('Logged in as Teacher')
    else:
        if request.GET.get('user'):
            return HttpResponse('User Code - ' + request.GET.get('user'))
        # decode.sign(user)
        return HttpResponse('Wrong Link')


        # decode.sign(user)