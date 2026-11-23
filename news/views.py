import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
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

def index(request):
    return render(request, "news/index.html")


def home (request):
    articoli = Articolo.objects.all()
    context = { 'articoli': articoli }
    return render(request, "news/homepage.html", context)


def articoloDetailView(request, pk):
    articolo = Articolo.objects.get(pk=pk)
    context = { 'articolo': articolo }
    return render(request, "news/articolo_detail.html", context)


def lista_articoli(request, giornalista_id):
    articoli = Articolo.objects.filter(giornalista_id=giornalista_id)
    context = { 'articoli': articoli }
    return render(request, "news/lista_articoli.html", context)

def queryBase(request):
    # 1. Tutti gli articoli scritti da giornalisti di un certo cognome:
    articoli_cognome = Articolo.objects.filter(giornalista__cognome='Rossi')

    # 2. Totale
    numero_totale_articoli = Articolo.objects.count()

    # 3. Contare il numero di articoli scritti da un giornalista specifico:
    giornalista_1 = Giornalista.objects.filter(id=1).first()
    numero_articoli_giornalista_1 = Articolo.objects.filter(giornalista_id=1).count()

    # 4. Ordinare gli articoli per numero di visualizzazioni in ordine decrescente:
    articoli_ordinati = Articolo.objects.order_by('-visualizzazioni')

    # 5. Tutti gli articoli che non hanno visualizzazioni:
    articoli_senza_visualizzazioni = Articolo.objects.filter(visualizzazioni=0)

    # 6. Articolo più visualizzato
    articolo_piu_visualizzato = Articolo.objects.order_by('-visualizzazioni').first()

    # 7. Tutti i giornalisti nati dopo una certa data:
    giornalisti_data = Giornalista.objects.filter(anno_nascita__gt=datetime.date(1990, 1, 1))

    # 8. Tutti gli articoli pubblicati in una data specifica:
    articoli_del_giorno = Articolo.objects.filter(data=datetime.date(2023, 1, 1))

    # 9. Tutti gli articoli pubblicati in un intervallo di date
    articoli_periodo = Articolo.objects.filter(
        data__range=(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31))
    )

    # 10. Gli articoli scritti da giornalisti nati prima del 1980:
    giornalisti_nati = Giornalista.objects.filter(anno_nascita__lt=datetime.date(1980, 1, 1))
    articoli_giornalisti = Articolo.objects.filter(giornalista__in=giornalisti_nati)

    # 11. Il giornalista più giovane:
    giornalista_giovane = Giornalista.objects.order_by('-anno_nascita').first()

    # 12. Il giornalista più anziano:
    giornalista_anziano = Giornalista.objects.order_by('anno_nascita').first()

    # 13. Gli ultimi 5 articoli pubblicati:
    ultimi = Articolo.objects.order_by('-data')[:5]

    # 14. Tutti gli articoli con un certo numero minimo di visualizzazioni:
    articoli_minime_visualizzazioni = Articolo.objects.filter(visualizzazioni__gte=100)

    # 15. Tutti gli articoli che contengono una certa parola nel titolo:
    articoli_parola = Articolo.objects.filter(titolo__icontains='importante')

    # 16. Articoli pubblicati a gennaio 2023:
    articoli_mese_anno = Articolo.objects.filter(data__month=1, data__year=2023)

    # 17. Giornalisti con almeno un articolo con 100 o più visualizzazioni:
    giornalisti_con_articoli_popolari = Giornalista.objects.filter(
        articoli__visualizzazioni__gte=100
    ).distinct()

    data_limite = datetime.date(1990, 1, 1)
    visualizzazioni_limite = 50

    # 18. Articoli il cui giornalista è nato dopo la data limite
    # e che hanno almeno 50 visualizzazioni:
    articoli_con_and = Articolo.objects.filter(
        giornalista__anno_nascita__gt=data_limite,
        visualizzazioni__gte=visualizzazioni_limite,
    )

    # 19. Articoli il cui giornalista è nato dopo la data limite
    # oppure che hanno al massimo 50 visualizzazioni:
    articoli_con_or = Articolo.objects.filter(
        Q(giornalista__anno_nascita__gt=data_limite)
        | Q(visualizzazioni__lte=visualizzazioni_limite)
    )

    # 20. Articoli il cui giornalista non è nato prima della data limite.
    articoli_con_not = Articolo.objects.filter(
        ~Q(giornalista__anno_nascita__lt=data_limite)
    )
    articoli_con_not_exclude = Articolo.objects.exclude(
        giornalista__anno_nascita__lt=data_limite
    )

    # Creare il dizionario context
    context = {
        'articoli_cognome': articoli_cognome,
        'numero_totale_articoli': numero_totale_articoli,
        'giornalista_1': giornalista_1,
        'numero_articoli_giornalista_1': numero_articoli_giornalista_1,
        'articoli_ordinati': articoli_ordinati,
        'articoli_senza_visualizzazioni': articoli_senza_visualizzazioni,
        'articolo_piu_visualizzato': articolo_piu_visualizzato,
        'giornalisti_data': giornalisti_data,
        'articoli_del_giorno': articoli_del_giorno,
        'articoli_periodo': articoli_periodo,
        'articoli_giornalisti': articoli_giornalisti,
        'giornalista_giovane': giornalista_giovane,
        'giornalista_anziano': giornalista_anziano,
        'ultimi': ultimi,
        'articoli_minime_visualizzazioni': articoli_minime_visualizzazioni,
        'articoli_parola': articoli_parola,
        'articoli_mese_anno': articoli_mese_anno,
        'giornalisti_con_articoli_popolari': giornalisti_con_articoli_popolari,
        'articoli_con_and': articoli_con_and,
        'articoli_con_or': articoli_con_or,
        'articoli_con_not': articoli_con_not,
        'articoli_con_not_exclude': articoli_con_not_exclude,
    }

    return render(request, 'news/query.html', context)