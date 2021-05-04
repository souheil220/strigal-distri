from django.urls import path

from . import views

urlpatterns = [
    path("listCommandesC", views.listCommandes, name="listCommandes"), 
    path("detailCommande/<str:id>", views.detailCommande, name="detailCommande"),]
