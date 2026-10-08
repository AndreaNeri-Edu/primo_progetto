from django.shortcuts import render
import datetime

# Create your views here.
def index_root(request):
    return render(request, "index_root.html")

def index_seconda(request):
    return render(request, "index_seconda.html")

def es_if(request):
    dic = {
        "var1": 200,
        "var2": 200,
        "var3": 300,
    }
    return render(request, "es_if.html", dic)

def es_if_else_elif(request):
    dic = {
        "var1": 200,
        "var2": 200,
        "var3": 300,
    }
    return render(request, "es_if_else_elif.html", dic)

def es_for(request):
    dic= {
        'list1': [1, datetime.date(2019,7,16), 'Do not give up'],
        'list2': [1, datetime.date(2019,7,16), 'Do not give up'],
        'my_dict': {'chiave1': 'Valore 1', 'chiave2': 'Valore 2'}
    }
    return render(request, "es_for.html", dic)