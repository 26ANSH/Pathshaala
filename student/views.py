from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def indexok(request):
    return HttpResponse("Hello, world. You're at the Student at ok index.")