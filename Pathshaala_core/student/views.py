from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1> Hello Student <h2>")

# Create your views here.
def basic(request):
    # return render(request, 'student/index.html')
    return HttpResponse("<h1> Hello Student <h2>")
