from django.shortcuts import render
def index(request):
    return render(request, 'myfirstapp/index.html')
def formulaire(request):
    return render(request, 'myfirstapp/formulaire.html')

def bonjour(request):
    nom=request.GET["nom"]
    prenom=request.GET["prenom"]
    return render(request, 'myfirstapp/bonjour.html', {"nom": nom}, {"prenom": prenom})