from django.http import HttpResponse
from django.shortcuts import render

def indextt(request):
    context = {'say': "Welcome to Pathshaala"}
    return render(request, 'landing.html')