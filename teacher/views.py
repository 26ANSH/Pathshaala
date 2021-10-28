from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'student/say.html', {'say':' Pathshaala ❤️ Teacher'})

# Create your views here.
