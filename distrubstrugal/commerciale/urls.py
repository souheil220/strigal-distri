from django.urls import path

from . import views

urlpatterns = [
    path("listCommandesC", views.listCommandes, name="listCommandes"), ]
