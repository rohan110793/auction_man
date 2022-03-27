from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

#this is views

def home(request):
    return HttpResponse("Hello, Django! and auction man")

# Testing git push