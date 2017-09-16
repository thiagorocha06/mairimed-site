from django.shortcuts import render, get_object_or_404, redirect
from .models import Termo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

### TERMOS ###

def lista_termos(request):
    lista_termos = Termo.objects.filter(definicao__isnull=False).order_by('nome')

    #Pesquisa
    termo_pesquisa = request.GET.get("campo_pesquisa")
    if termo_pesquisa:
        lista_termos = lista_termos.filter(nome__icontains=termo_pesquisa)

    #Paginacao
    paginator = Paginator(lista_termos, 25) # Show 5 contacts per page
    page_request_var = "pagina"
    page = request.GET.get(page_request_var)
    try:
        termos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        termos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        termos = paginator.page(paginator.num_pages)

    conteudo = {
        'termos' : termos,
        'page_request_var': page_request_var
    }

    return render(request, 'termos/lista_termos.html', conteudo)

def detalhe_termos(request, pk):
    termo = get_object_or_404(Termo, pk=pk)
    return render(request, 'termos/detalhe_termos.html', {'termo': termo})
