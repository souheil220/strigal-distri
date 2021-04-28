from django.urls import path

from . import views

urlpatterns = [
    path("commande", views.commande, name="commande"),
    path("listCommandesD", views.listCommandes, name="listCommandesD"), 
    path("getProduct", views.getProduct, name="getProduct"), 
    
    ]
