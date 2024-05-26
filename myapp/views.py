from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

# Create your views here.

url_data = {
    "computer": "Computer Category",
    "phone": "Phone Category",
    "electronic": "Electronic Category",
}

# http://localhost:8000
def index(request):
    return HttpResponse("Hello World!")

def detail(request):
    return HttpResponse("Detail")

def getProductByCategory(request, category):
    '''category_text = None

    if category == "computer":
        category_text = "Computer Category"
    
    elif category == "phone":
        category_text = "Phone Category"

    else:
        category_text = "Wrong Category"

    return HttpResponse(category_text)'''

    try:
        category_text = url_data[category]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("Wrong Category")

def getProductByCategoryId(request, category_id):
    #return HttpResponse(category)
    #return HttpResponseRedirect("/products/computer") #redirect, HttpResponseRedirect("computer") works too
    #return redirect("/products/computer")

    category_list = list(url_data.keys())

    if category_id > len(category_list):
        return HttpResponseNotFound("Wrong Category")

    redirect_text = category_list[category_id-1]

    return redirect("/products/"+ redirect_text)