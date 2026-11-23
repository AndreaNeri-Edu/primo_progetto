from django.urls import path
from .views import index, home, articoloDetailView, giornalistaDetailView, lista_articoli, queryBase

app_name="news"
urlpatterns=[
    path('', index, name='index'),
    path('home/', home, name='homeviews'),
    path('lista_articoli/', lista_articoli, name='lista_articoli'),
    path("lista_articoli/<int:giornalista_id>", lista_articoli, name="lista_articoli_giornalista"),
    path("lista_giornalisti/", giornalistaDetailView, name="lista_giornalisti"),
    path("giornalisti/", giornalistaDetailView, name="giornalisti"),
    path("articoli/<int:pk>", articoloDetailView, name='articolo_detail'),
    path("giornalisti/<int:pk>", giornalistaDetailView, name='giornalista_detail'),
    path('query_base/', queryBase, name='query_base'),
]