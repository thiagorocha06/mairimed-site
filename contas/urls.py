from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'contas/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'contas/logout.html'}, name='logout'),
    url(r'^cadastro/$', views.cadastro, name='cadastro'),
    url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^perfil/editar$', views.editar_perfil, name='editar_perfil'),
]
