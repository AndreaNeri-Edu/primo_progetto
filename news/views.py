from django.shortcuts import render
from django.http import HttpResponse
from .models import Articolo, Giornalista

# Create your views here.
"""
1. Con questa view, quando l'utente accede alla pagina /news/ la pagina risponde con il titolo "Homepages News!".

def home (request):
    return HttpResponse("<h1>Homepages News!</h1>") 


2. Con questa view, quando l'utente accede alla pagina /news/ la pagina risponde facendo un ciclo for su tutti gli articoli e giornalisti presenti nel database,
stampando i titoli degli articoli e i nomi dei giornalisti.

def home (request):
    a = ""
    g = ""

    for art in Articolo.objects.all():
       a += (art.titolo + "<br>")

    for gio in Giornalista.objects.all():
       g += (gio.nome + "<br>")

    response = "Articoli:<br>" + a + "Giornalisti:<br>" + g

    return HttpResponse(f"<h1>" + response + "</h1>")

3. Con questa view, quando l'utente accede alla pagina /news/ la pagina risponde importando i titoli degli articoli e i nomi dei giornalisti in due liste separate,
per poi stampampare le due liste.

def home (request):
    a = []
    g = []

    for art in Articolo.objects.all():
       a.append(art.titolo)
    for gio in Giornalista.objects.all():
        g.append(gio.nome)

    response = str(a) + "<br>" + str(g)
    print(response)

    return HttpResponse(f"<h1>" + response + "</h1>")
"""

def home (request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()

    context = { "articoli": articoli, "giornalisti": giornalisti }
    print(context)

    return render(request, "news/homepage.html", context)


def articoloDetailView(request, pk):
    articolo = Articolo.objects.get(pk=pk)
    context = { "articolo": articolo }
    return render(request, "news/articolo_detail.html", context)