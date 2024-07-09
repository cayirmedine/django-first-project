from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
from datetime import datetime
from .models import Product
from django.db.models import Avg, Min, Max

# Create your views here.

'''url_data = {
    "computer": ["comp1", "comp2"],
    "phone": ["phone1", "phone2"],
    "electronic": []
}'''

# http://localhost:8000
def index(request):
    # categories = list(url_data.keys())

    '''list_items = ""

    for category in categories:
        redirect_path = reverse("products_by_category", args=[category])
        list_items += f"<li><a href='{redirect_path}'>{category}</a></li>"

    html = f"<ul>{list_items}</ul>"

    return HttpResponse(html)'''

    products = Product.objects.all().order_by("-price")
    product_count = Product.objects.filter(is_active=True).count()
    price_calcs = Product.objects.filter(is_active=True).aggregate(Avg('price'), Min('price'), Max('price'))

    context = {
        "products": products,
        "product_count": product_count,
        "price_calcs": price_calcs
    }

    # return render(request, "myapp/index.html") #In seetings.py file templates defined as template path so myapp/ necessary

    return render(request, "index.html", context)

def details(request, slug):

    '''try:
        product = Product.objects.get(pk=id) # id=id can be used too

    except:
        raise Http404()'''
    

    # product = get_object_or_404(Product, pk=id)

    product = get_object_or_404(Product, slug=slug)

    context = {
        "product": product
    }

    return render(request, "details.html", context)

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
        products = url_data[category]
        #return HttpResponse(category_text)
        #return HttpResponse(f"<h1>{category_text}</h1>")

        return render(request, "products.html", { #These html files moved to app's templates directory, we dont need myapp/ anymore
            "category": category,
            "products": products,
            "now": datetime.now
        }) # pass args to the page
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

    