from django.urls import path
from . import views #use a file from same directory

urlpatterns = [
    path("", views.index, name='index'),
    path("index", views.index, name='index'),
    path("list", views.list, name='list'),
    path("detail", views.detail, name='detail')
]
