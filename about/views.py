from django.shortcuts import render
from django.http import request, HttpResponse
# Create your views here.

def about(request):
    return render(request, 'about/about.html')