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
from .firebase import student_login
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

def index_student(request):
    if student_auth(request):
        return render(request, 'student/say.html', {'say': f' Pathshaala ❤️ {request.user.first_name}'})
    elif is_teacher(request):
        return HttpResponse('Logged in as Teacher')
    else:
        return redirect('/student/auth/login/?error=Login to Access !!!')

def login_student(request):
    if student_auth(request):
        return redirect('index')
    elif is_teacher(request):
        return redirect('/student/auth/login/?error=Logged in as Teacher !!!')
    else:
        if request.method == 'POST':
            form = request.POST
            email=form['email']
            password=form['password']
            user = student_login(email, password)
            print(form, user)
            if user == 400:
                return redirect('/student/auth/login/?error=Wrong Credentials !!!')

            print('student_'+user)
            auth_user = authenticate(username='student_'+user, password=password)
            login(request, auth_user)
            return redirect('index_student')
        else:
            if request.GET.get('error'):
                error = request.GET.get('error')
                return render(request,'student/login.html', {'error':error})
            elif request.GET.get('alert'):
                alert = request.GET.get('alert')
                return render(request,'student/login.html', {'alert':alert})
            
            return render(request, 'student/login.html')

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

def logout_student(request):
    logout(request)
    return redirect('/student/auth/login/?alert=Logged Out Sucessfully !!!')