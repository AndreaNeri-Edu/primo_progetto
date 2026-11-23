from django.urls import path
from .views import index, home, articoloDetailView, lista_articoli, queryBase

app_name="news"
urlpatterns=[
    path('', index, name='index'),
    path('lista_articoli/', home, name='homeviews'),
    path("lista_articoli/<int:giornalista_id>", lista_articoli, name="lista_articoli"),
    path("articoli/<int:pk>", articoloDetailView, name='articolo_detail'),
    path('query_base/', queryBase, name='query_base'),
]