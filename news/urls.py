from django.urls import path
from .views import home, articoloDetailView, lista_articoli

app_name="news"
urlpatterns=[
    path('lista_articoli/', home, name='homeviews'),
    path("lista_articoli/<int:giornalista_id>", lista_articoli, name="lista_articoli"),
    path("articoli/<int:pk>", articoloDetailView, name='articolo_detail'),
]