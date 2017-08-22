from django.shortcuts import render
from django.utils import timezone
from .models import Artigo
from django.shortcuts import render, get_object_or_404
from .forms import ArtigoForm
from django.shortcuts import redirect

def lista_artigos(request):
    artigos	=	Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/lista_artigos.html', {'artigos' : artigos})

def detalhe_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    return render(request, 'artigos/detalhe_artigo.html', {'artigo': artigo})

def novo_artigo(request):
    if request.method == "POST":
        form = ArtigoForm(request.POST)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.author = request.user
            artigo.data_de_publicacao = timezone.now()
            artigo.save()
            return redirect('detalhe_artigo', pk=artigo.pk)
    else:
        form = ArtigoForm()
    return render(request, 'artigos/edicao_artigo.html', {'form': form})

def edicao_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if request.method == "POST":
        form = ArtigoForm(request.POST, instance=artigo)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.author = request.user
            artigo.published_date = timezone.now()
            artigo.save()
            return redirect('detalhe_artigo', pk=artigo.pk)
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'artigos/edicao_artigo.html', {'form': form})
