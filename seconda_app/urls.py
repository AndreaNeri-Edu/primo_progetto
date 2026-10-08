from django.urls import path
from seconda_app.views import index_seconda, es_if, es_if_else_elif, es_for

app_name="seconda_app"
urlpatterns=[
    path('', index_seconda, name='index_seconda'),
    path('es_if', es_if, name='es_if'),
    path('es_if_else_elif', es_if_else_elif, name='es_if_else_elif'),
    path('es_for', es_for, name='es_for')
]