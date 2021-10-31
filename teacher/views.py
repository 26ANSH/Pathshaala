from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .firebase import create_user, teacher_login
from .models import _new_user

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

# Create your views here.
def signin(request):
    if not teacher_auth(request):
        if request.method == 'POST':
            form = request.POST
            user = create_user(form['email'], form['password'])
            if user == 400:
                return HttpResponse('User already exists')
            else:
                # sync_to_async(_new_user, thread_sensitive=True)
                _new_user(user,form['name'], form['email'])
                User.objects.create_user(first_name = form['name'].split(' ')[0], last_name = form['name'].split(' ')[1], username='teacher_'+user, password=form['password'], email=form['email'])
                authenticated_user = authenticate(username='teacher_'+user, password=form['password'])
                login(request, authenticated_user)
                return HttpResponse('User created and authenticated')
        else:    
            return render(request,'teacher/signup.html')
    else:
        return redirect('/teacher')

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
                return HttpResponse('Invalid credentials, Try again')
        else:
            return render(request,'teacher/login.html')
    else:
        return redirect('index')
        
def my_logout(request):
    if teacher_auth(request):
        logout(request)

    return redirect('index')

# def add_student(request)