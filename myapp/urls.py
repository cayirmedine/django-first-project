from django.urls import path
from . import views #use a file from same directory

urlpatterns = [
    path("", views.index)
]
