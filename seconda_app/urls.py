from django.urls import path
from seconda_app.views import index_seconda, es_if

app_name="seconda_app"
urlpatterns=[
    path('', index_seconda, name='index_seconda'),
    path('es_if', es_if, name='es_if')
]