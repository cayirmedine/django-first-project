from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

# http://localhost:8000
def index(request):
    return HttpResponse("Hello World!")
