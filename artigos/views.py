from django.shortcuts import render, HttpResponse
from django.utils import timezone
from .models import Artigo
from django.shortcuts import render, get_object_or_404
from .forms import ArtigoForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import DicioMed

def inicio(request):
    return render(request, 'mairimed/inicio.html')

def lista_termos(request):
    termos = DicioMed.objects.filter(definicao__isnull=False).order_by('nome')
    return render(request, 'termos/lista_termos.html', {'termos' : termos})

def lista_artigos(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/lista_artigos.html', {'artigos' : artigos})

def detalhe_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    return render(request, 'artigos/detalhe_artigo.html', {'artigo': artigo})

@login_required
def novo_artigo(request):
    if request.method == "POST":
        form = ArtigoForm(request.POST)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.author = request.user
            artigo.save()
            return redirect('detalhe_artigo', pk=artigo.pk)
    else:
        form = ArtigoForm()
    return render(request, 'artigos/edicao_artigo.html', {'form': form})

@login_required
def edicao_artigo(request, pk):
    artigo = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ArtigoForm(request.POST, instance=post)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.author = request.user
            artigo.save()
            return redirect('detalhe_artigo', pk=artigo.pk)
    else:
        form = ArtigoForm(instance=post)
    return render(request, 'artigos/edicao_artigo.html', {'form': form})

@login_required
def lista_rascunhos(request):
	artigos = Artigo.objects.filter(data_de_publicacao__isnull=True).order_by('data_de_criacao')
	return render(request, 'artigos/lista_rascunhos.html', {'artigos': artigos})

@login_required
def publicar_artigo(request,	pk):
	artigo = get_object_or_404(Artigo, pk=pk)
	artigo.publicar()
	return redirect('detalhe_artigo', pk=pk)

@login_required
def	remover_artigo(request,	pk):
	artigo = get_object_or_404(Artigo, pk=pk)
	artigo.delete()
	return redirect('lista_artigos')
