from django.urls import path

from . import views

urlpatterns = [
    path("commande", views.commande, name="commande"),
    path("listCommandesD", views.listCommandes, name="listCommandesD"),
    path("modifierMP", views.modifierMP, name="modifierMP"),
    path("detailCommande/<str:id>", views.detailCommande, name="detailCommande"),
    path("loadMore/<str:name>/<str:whiche>", views.loadMore, name="loadMore"),
    path("filterer/<str:etat>/<str:date>", views.filterer, name="filterer"),
    path("regCommand", views.regCommand, name="regCommand"),
    path('pdf_view/<int:id>', views.render_to_pdf, name='pdf_view'),
]
