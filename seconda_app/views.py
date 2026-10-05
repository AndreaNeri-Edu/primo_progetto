from django.shortcuts import render

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