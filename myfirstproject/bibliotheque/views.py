from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LivreForm
from . import models


def index(request):
    liste = list(models.Livre.objects.all())
    return render(request, "bibliotheque/index.html", {"liste": liste})


def ajout(request):
    if request.method == "POST":
        form = LivreForm(request.POST)
        if form.is_valid():
            Livre = form.save()
            return render(request, "bibliotheque/affiche.html", {"Livre": Livre})
        else:
            return render(request, "bibliotheque/ajout.html", {"form": form})
    else:
        form = LivreForm()
        return render(request, "bibliotheque/ajout.html", {"form": form})


def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save()
        return render(request, "bibliotheque/affiche.html", {"Livre": Livre})
    else:
        return render(request, "bibliotheque/ajout.html", {"form": lform})


def read(request, id):
    Livre = models.Livre.objects.get(pk=id)
    return render(request, "bibliotheque/affiche.html", {"Livre": Livre})


def update(request, id):
    Livre = models.Livre.objects.get(pk=id)
    dictionnaire = {
        "titre": Livre.titre,
        "auteur": Livre.auteur,
        "date_parution": Livre.date_parution,
        "nombre_pages": Livre.nombre_pages,
        "resume": Livre.resume,
    }
    lform = LivreForm(dictionnaire)
    return render(request, "bibliotheque/update.html", {"form": lform, "id": id})


def traitementupdate(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save(commit=False)
        Livre.id = id
        Livre.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request, "bibliotheque/update.html", {"form": lform, "id": id})


def delete(request, id):
    Livre = models.Livre.objects.get(pk=id)
    Livre.delete()
    return HttpResponseRedirect("/bibliotheque/")
