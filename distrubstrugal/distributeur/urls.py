from django.urls import path

from . import views

urlpatterns = [
    path("commande", views.commande, name="commande"),
    path("listCommandesD", views.listCommandes, name="listCommandesD"),
    path("detailCommande/<str:id>", views.detailCommande, name="detailCommande"),
    path("loadMore/<str:name>/<str:whiche>", views.loadMore, name="loadMore"),
    path("regCommand", views.regCommand, name="regCommand"),
    # path('pdf_view/', views.ViewPDF.as_view(), name='pdf_view'),
    path('pdf_view/<int:id>', views.render_to_pdf, name='pdf_view'),
]
