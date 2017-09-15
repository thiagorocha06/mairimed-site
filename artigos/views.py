from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Artigo, Termo, Farmaco
from contas.models import Estudante
from .forms import ArtigoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def inicio(request):
    estudante = Estudante.objects
    lista_artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('-data_de_publicacao')
    paginator = Paginator(lista_artigos, 5) # Show 5 contacts per page
    page_request_var = "pagina"
    page = request.GET.get(page_request_var)
    try:
        artigos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        artigos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        artigos = paginator.page(paginator.num_pages)

    termo_pesquisa = request.GET.get("campo_pesquisa")
    if termo_pesquisa:
        lista_artigos = lista_artigos.filter(titulo__icontains=termo_pesquisa)

    conteudo = {
        'lista_artigos': artigos,
        'estudante': estudante,
        'page_request_var': page_request_var
    }

    return render(request, 'mairimed/inicio.html', conteudo)

### TERMOS ###

def lista_termos(request):
    termos = Termo.objects.filter(definicao__isnull=False).order_by('nome')
    return render(request, 'termos/lista_termos.html', {'termos' : termos})

def detalhe_termos(request, pk):
    termo = get_object_or_404(Termo, pk=pk)
    return render(request, 'termos/detalhe_termos.html', {'termo': termo})

### FARMACOS ###

def lista_farmacos(request):
    farmacos = Farmaco.objects.filter(nome__isnull=False).order_by('nome')
    return render(request, 'farmacos/lista_farmacos.html', {'farmacos' : farmacos})

def detalhe_farmacos(request, pk):
    farmaco = get_object_or_404(Farmaco, pk=pk)
    return render(request, 'farmacos/detalhe_farmacos.html', {'farmaco': farmaco})

### ARTIGOS ###

def categorias_artigos(request):
    return render(request, 'artigos/categorias_artigos.html')

def infectologia_artigos(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/categorias/infectologia_artigos.html', {'artigos' : artigos})

def cardiologia_artigos(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/categorias/cardiologia_artigos.html', {'artigos' : artigos})

def endocrinologia_artigos(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/categorias/endocrinologia_artigos.html', {'artigos' : artigos})

def nefrologia_artigos(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/categorias/nefrologia_artigos.html', {'artigos' : artigos})

def pediatria_artigos(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/categorias/pediatria_artigos.html', {'artigos' : artigos})

def pneumologia_artigos(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/categorias/pneumologia_artigos.html', {'artigos' : artigos})

def detalhe_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    estudante = Estudante.objects
    return render(request, 'artigos/detalhe_artigo.html', {'estudante': estudante, 'artigo': artigo})

def favoritos_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    artigos_favoritos = Estudante.artigos_favoritos
    estudante = Estudante.objects
    estudante.artigos_favoritos.add(artigo)
    return redirect('detalhe_artigo', pk=pk)

### ESCS ###

def p_serie(request):
    return render(request, 'artigos/ESCS/1_serie.html')

def s_serie(request):
    return render(request, 'artigos/ESCS/2_serie.html')

def t_serie(request):
    return render(request, 'artigos/ESCS/3_serie.html')

def q_serie(request):
    return render(request, 'artigos/ESCS/4_serie.html')

def M401(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/ESCS/M401.html', {'artigos' : artigos})

def M402(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/ESCS/M402.html', {'artigos' : artigos})

def M403(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/ESCS/M403.html', {'artigos' : artigos})

def M404(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/ESCS/M404.html', {'artigos' : artigos})

def M406(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/ESCS/M406.html', {'artigos' : artigos})

def M407(request):
    artigos = Artigo.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'artigos/ESCS/M407.html', {'artigos' : artigos})

### Deletar daqui para baixo ###


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
def publicar_artigo(request, pk):
	artigo = get_object_or_404(Artigo, pk=pk)
	artigo.publicar()
	return redirect('detalhe_artigo', pk=pk)

@login_required
def	remover_artigo(request,	pk):
	artigo = get_object_or_404(Artigo, pk=pk)
	artigo.delete()
	return redirect('lista_artigos')
