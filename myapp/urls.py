from django.urls import path
from . import views #use a file from same directory

urlpatterns = [
    path("", views.index, name='index'),
    path("index", views.index, name='index'),
    path("list", views.list, name='list'),
    path("detail", views.detail, name='detail'),
    #path('<category>', views.getProductByCategory) #dynamic path
    path('<int:category>', views.getProductByCategoryId), #accepts only int value as a parameter
    path('<str:category>', views.getProductByCategory) #accpets only str value as a parameter, but everything can be count as a str
    #if str parameter define before int, int parameters never go into getProductByCategoryId
]
