from django.shortcuts import render, redirect
from contas.formularios import FormularioCadastro
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

def cadastro(request):
    if request.method == "POST":
        form = FormularioCadastro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FormularioCadastro()

        args = {'form' : form}
        return render(request, 'contas/cadastro.html', args)

def perfil(request):
    args = {'user': request.user}
    return render(request, 'contas/perfil.html')

def editar_perfil(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/perfil')

    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'contas/editar_perfil.html', args)
