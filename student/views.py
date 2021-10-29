from django.http import HttpResponse
from django.shortcuts import render

import random
# login authenticate module in django.contrib

def index(request):
    if request.user.is_authenticated:
        return render(request, 'student/say.html', {'say':f'{request.user.first_name} Welcome to Pathshaala'})
    else:
        return render(request, 'student/say.html', {'say':'GuestWelcome to Pathshaala'})