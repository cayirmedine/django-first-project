from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

# Create your views here.

url_data = {
    "computer": "Computer Category",
    "phone": "Phone Category",
    "electronic": "Electronic Category",
}

# http://localhost:8000
def index(request):
    categories = list(url_data.keys())

    list_items = ""

    for category in categories:
        redirect_path = reverse("products_by_category", args=[category])
        list_items += f"<li><a href='{redirect_path}'>{category}</a></li>"

    html = f"<ul>{list_items}</ul>"

    return HttpResponse(html)

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
        #return HttpResponse(category_text)
        return HttpResponse(f"<h1>{category_text}</h1>")
    except:
        return HttpResponseNotFound("<h1>Wrong Category</h1>")

def getProductByCategoryId(request, category_id):
    #return HttpResponse(category)
    #return HttpResponseRedirect("/products/computer") #redirect, HttpResponseRedirect("computer") works too
    #return redirect("/products/computer")

    category_list = list(url_data.keys())

    if category_id > len(category_list):
        return HttpResponseNotFound("Wrong Category")

    #redirect_text = category_list[category_id-1]

    #return redirect("/products/"+ redirect_text)

    category_text = category_list[category_id - 1]

    redirect_path = reverse("products_by_category", args=[category_text]) #redirect path with name info

    return redirect(redirect_path)

    