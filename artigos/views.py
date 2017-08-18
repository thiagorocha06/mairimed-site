from django.shortcuts import render
from django.utils import timezone
from .models import Artigo

def lista_artigos(request):
    artigos	=	Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/lista_artigos.html', {'artigos' : artigos})
