from django.urls import path
from prova_pratica_1_B.views import index_prova_pratica_1_B, massimo, pari, studenti

app_name="prova_pratica_1_B"
urlpatterns=[
    path('', index_prova_pratica_1_B, name='index_prova_pratica_1_B'),
    path('view_x', massimo, name='massimo'),
    path('view_y', pari, name='pari'),
    path('view_z', studenti, name='studenti')
]