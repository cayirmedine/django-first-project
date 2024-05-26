from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

# http://localhost:8000
def index(request):
    return HttpResponse("Hello World!")

def list(request):
    return HttpResponse("List")

def detail(request):
    return HttpResponse("Detail")

def getProductByCategory(request, category):
    category_text = None

    if category == "computer":
        category_text = "Computer Category"
    
    elif category == "phone":
        category_text = "Phone Category"

    else:
        category_text = "Wrong Category"

    return HttpResponse(category_text)

def getProductByCategoryId(request, category):
    return HttpResponse(category)
