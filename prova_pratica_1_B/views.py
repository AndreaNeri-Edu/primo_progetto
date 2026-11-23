from django.shortcuts import render
import random

# Create your views here.
def index_root(request):
    return render(request, "index_root.html")

def index_prova_pratica_1_B(request):
    return render(request, "index_prova_pratica_1_B.html")

def massimo(request):
    dic = { 
        "var1": random.randint(1, 20),
        "var2": random.randint(1, 20),
        "var3": random.randint(1, 20),
    }
    return render(request, "view_x.html", dic)

def pari(request):
    lista1 = [random.randint(1, 20) for i in range(0, 30)]
    pari = 0

    for i in range(0, 30):
        if lista1[i] % 2 == 0:
            pari += 1
    
    dic = {"lista1": lista1, "pari": pari}    
    return render(request, "view_y.html", dic)    

def studenti(request):
    return render(request, "view_z.html") 