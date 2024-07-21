from django.urls import path
from . import views #use a file from same directory

urlpatterns = [
    path("", views.index),
    path("index", views.index, name='index'),
    #path("<int:id>", views.details),
    path("list", views.list),
    path("create", views.create),
    path("<slug:slug>", views.details, name="product-details"),
    #path('<category>', views.getProductByCategory) #dynamic path
    #path('<int:category_id>', views.getProductByCategoryId), #accepts only int value as a parameter
    #path('<str:category>', views.getProductByCategory, name="products_by_category"), #accpets only str value as a parameter, but everything can be count as a str
    #if str parameter define before int, int parameters never go into getProductByCategoryId
]
