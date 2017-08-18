from django.shortcuts import render
from django.utils import timezone
from .models import Artigo
from django.shortcuts import render, get_object_or_404

def lista_artigos(request):
    artigos	=	Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/lista_artigos.html', {'artigos' : artigos})

def detalhe_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    return render(request, 'artigos/detalhe_artigo.html', {'artigo': artigo})
