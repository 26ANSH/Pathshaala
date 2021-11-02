from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .firebase import create_user, teacher_login
from .models import _new_user
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
import asyncio
from asgiref.sync import sync_to_async
from django.contrib.auth.decorators import login_required


def teacher_auth(request):
    if request.user.is_authenticated and request.user.username.split('_')[0]=='teacher':
        return True
    else:
        return False

def index(request):
    if teacher_auth(request):
        return render(request, 'student/say.html', {'say': f' Pathshaala ❤️ {request.user.first_name}'})
    else:
        return redirect('login')

async def signin(request):
    if not await sync_to_async(teacher_auth)(request):
        if request.method == 'POST':
            form = request.POST
            user = await sync_to_async(create_user)(form['email'], form['password'])
            if user == 400:
                print(user)
                return HttpResponse('User already exists')
            else:
                token = await sync_to_async(_new_user)(user,form['fname'],form['lname'], form['email'], form['country'], form['gender'])
                await sync_to_async(User.objects.create_user)(first_name = form['fname'], last_name = form['lname'], username='teacher_'+user, password=form['password'], email=form['email'])
                authenticated_user = await sync_to_async(authenticate)(username='teacher_'+user, password=form['password'])
                msg = render_to_string('mail.html', {'header':'Welcome to Pathshaala👨‍💻🔥', 'name': form['fname'],'otp':token, 'email':form['email']})
                email = EmailMessage(
                    'Welcome to Pathshaala', 
                    msg,
                    settings.EMAIL_HOST_USER,
                    [form['email']]
                )
                email.content_subtype = 'html'
                email.fail_silently = False
                mail = sync_to_async(email.send)
                asyncio.create_task(mail())
                # authenticated_user.is_active = False
                # await sync_to_async(authenticated_user.save)()
                await sync_to_async(login)(request, authenticated_user)
                return redirect('index')
        else:    
            return render(request,'teacher/signup.html')
    else:
        return redirect('index')

def User_Login(request):
    if not teacher_auth(request):
        if request.method == 'POST':
            form = request.POST
            email=form['email']
            password=form['password']
            username = teacher_login(email, password)
            if username != 400:
                authenticated_user = authenticate(username='teacher_'+username, password=password)
                login(request, authenticated_user)
                return redirect('index')
            else:
                # return HttpResponse('Invalid credentials, Try again')
                return render(request,'teacher/login.html', {'error' : 'Wrong Email or Psssword ! Retry'})
                # return redirect('/teacher/auth/login/?error=Wrong Email or Psssword ! Retry')
        else:
            # if request.GET.get('error'):
                # return render(request,'teacher/login.html', {'error':request.GET.get('error')})
            return render(request,'teacher/login.html')
    else:
        return redirect('index')
        
def my_logout(request):
    if teacher_auth(request):
        logout(request)

    return redirect('index')

# def add_student(request)

@login_required
def securepage(request):
    return HttpResponse('dashboard')

# def verifyemail(request):
#     if request.method == 'POST':
#         return HttpResponse('Post Method')
#     else:
#         if request.GET.get('code') and request.GET.get('email'):
#             return HttpResponse('Code {} Email {}'.format(request.GET.get('code'), request.GET.get('email')))
#         else:
#             return HttpResponse('Get Method')