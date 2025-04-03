from django.shortcuts import render
from .forms import LivreForm
from . import models

def ajout(request):
        form = LivreForm()  # création d'un formulaire vide
        return render(request, "biblioteque/ajout.html", {"form": form})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save()
        return render(request,"biblioteque/affiche.html",{"Livre" : Livre})
    else:
        return render(request,"biblioteque/ajout.html",{"form": lform})


def read(request, id):
    Livre = models.Livre.objects.get(pk=id)
    return render(request,"bibliotheque/affiche.html",{"Livre": Livre})

def update(request):
    Livre = models.Livre.objects.get(pk=id)
    return render(models, makedico)

def traitementupdate(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save(commit=False)
        Livre.id = id;
        Livre.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request, "bibliotheque/update.html", {"form": lform, "id": id})