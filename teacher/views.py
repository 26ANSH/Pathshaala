from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'teacher/t.html', {'say':' Pathshaala ❤️ Teacher'})

# Create your views here.
