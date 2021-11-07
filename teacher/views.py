from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .firebase import create_user, teacher_login
from .models import _new_user, get_token
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
import asyncio
from asgiref.sync import sync_to_async
from django.core.signing import Signer


def page_not_found_view(request, exception):
    return render(request, 'error/404.html', status=404)

decode = Signer()

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
                print(authenticated_user)
                msg = render_to_string('mail.html', {'header':'Welcome to Pathshaala👨‍💻🔥', 'name': form['fname'],'link':'https://pathshaala.azurewebsites.net/teacher/auth/verify/?user={}&code={}'.format(decode.sign(user), decode.sign(token)), 'email':form['email']})
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
                authenticated_user.is_active = False
                await sync_to_async(authenticated_user.save)()
                # await sync_to_async(login)(request, authenticated_user)
                return redirect('/teacher/auth/login/?alert=Account Created! Please Verify to continue, Link sent via email')
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
                id =  'teacher_'+username
                user = User.objects.get(username=id)
                if user.is_active:
                    authenticated_user = authenticate(username=id, password=password)
                    login(request, authenticated_user)
                    return redirect('dashboard')
                else:
                    return redirect("/teacher/auth/login/?error=Please Verify to continue, Link sent via email at {}".format(email))
            else:
                # return HttpResponse('Invalid credentials, Try again')
                # return render(request,'teacher/login.html', {'error' : 'Wrong Email or Psssword ! Retry'})
                return redirect('/teacher/auth/login/?error=Wrong Email or Password! Please retry!')
        else:
            if request.GET.get('error'):
                error = request.GET.get('error')
                return render(request,'teacher/login.html', {'error':error})
            elif request.GET.get('alert'):
                alert = request.GET.get('alert')
                return render(request,'teacher/login.html', {'alert':alert})
            
            return render(request,'teacher/login.html')
    else:
        return redirect('dashboard')

def my_logout(request):
    if teacher_auth(request):
        logout(request)

    return redirect('indextt')

# def add_student(request)

def securepage(request):
    if teacher_auth(request):
        return render(request, 'teacher/teacher_template.html')
    else:
        return redirect('/teacher/auth/login/?error=Login to Access')

# def verifyemail(request):
#     if request.method == 'POST':
#         return HttpResponse('Post Method')
#     else:
#         if request.GET.get('code') and request.GET.get('email'):
#             return HttpResponse('Code {} Email {}'.format(request.GET.get('code'), request.GET.get('email')))
#         else:
#             return HttpResponse('Get Method')

def verifyemail(request):
    if request.GET.get('code') and request.GET.get('user'):
        try:
            id = decode.unsign(request.GET.get('user'))
            code = decode.unsign(request.GET.get('code'))
            username='teacher_'+id
            user = User.objects.get(username=username)
        except:
            return redirect('/teacher/auth/login/?error=INVALID LINK')

        if user.is_active:
            return redirect('/teacher/auth/login/?alert=Email Already Verified')
        else:
            if int(code) == int(get_token(id)):
                user.is_active = True
                user.save()
                return redirect('/teacher/auth/login/?alert=Email Verified! Now you can Login to your account')
            else:
                return redirect('/teacher/auth/login/?error=INVALID LINK')
    else:
        return redirect('/teacher/auth/login/?error=INVALID LINK')