from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .firebase import create_user

def teacher_auth(request):
    if request.user.is_authenticated and request.user.username.split('_')[0]=='teacher':
        return True
    else:
        return False

def index(request):
    if teacher_auth(request):
        return render(request, 'student/say.html', {'say': f' Pathshaala ❤️ {request.user.first_name}'})
    else:
        return redirect('signin')

# Create your views here.
def signin(request):
    if not teacher_auth(request):
        if request.method == 'POST':
            form = request.POST
            user = create_user(form['email'], form['password'])
            if user == 400:
                return HttpResponse('User already exists')
            else:
                User.objects.create_user(first_name = form['name'].split(' ')[0], last_name = form['name'].split(' ')[1], username='teacher_'+user, password=form['password'], email=form['email'])
                authenticated_user = authenticate(username='teacher_'+user, password=form['password'])
                login(request, authenticated_user)
                return HttpResponse('User created and authenticated')
        else:    
            return render(request,'teacher/signin.html')
    else:
        return redirect('/teacher')

        
def my_logout(request):
    if teacher_auth(request):
        logout(request)

    return redirect('signin')