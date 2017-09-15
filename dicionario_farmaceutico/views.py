from django.shortcuts import render, get_object_or_404, redirect
from .models import Farmaco

### FARMACOS ###

def lista_farmacos(request):
    farmacos = Farmaco.objects.filter(nome__isnull=False).order_by('nome')
    #Pesquisa
    termo_pesquisa = request.GET.get("campo_pesquisa")
    if termo_pesquisa:
        farmacos = farmacos.filter(nome__icontains=termo_pesquisa)

    return render(request, 'farmacos/lista_farmacos.html', {'farmacos' : farmacos})

def detalhe_farmacos(request, pk):
    farmaco = get_object_or_404(Farmaco, pk=pk)
    return render(request, 'farmacos/detalhe_farmacos.html', {'farmaco': farmaco})
