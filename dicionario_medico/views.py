from django.shortcuts import render, get_object_or_404, redirect
from .models import Termo

### TERMOS ###

def lista_termos(request):
    termos = Termo.objects.filter(definicao__isnull=False).order_by('nome')

    #Pesquisa
    termo_pesquisa = request.GET.get("campo_pesquisa")
    if termo_pesquisa:
        termos = termos.filter(nome__icontains=termo_pesquisa)

    return render(request, 'termos/lista_termos.html', {'termos' : termos})

def detalhe_termos(request, pk):
    termo = get_object_or_404(Termo, pk=pk)
    return render(request, 'termos/detalhe_termos.html', {'termo': termo})
