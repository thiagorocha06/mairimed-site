from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),

    url(r'^artigo/categorias/$', views.categorias_artigos, name='categorias_artigos'),
    url(r'^artigo/abdome/$', views.abdome_artigos, name='abdome_artigos'),
    url(r'^artigo/cardiologia/$', views.cardiologia_artigos, name='cardiologia_artigos'),
    url(r'^artigo/endocrinologia/$', views.endocrinologia_artigos, name='endocrinologia_artigos'),
    url(r'^artigo/nefrologia/$', views.nefrologia_artigos, name='nefrologia_artigos'),
    url(r'^artigo/pediatria/$', views.pediatria_artigos, name='pediatria_artigos'),
    url(r'^artigo/pneumologia/$', views.pneumologia_artigos, name='pneumologia_artigos'),

    url(r'^artigo/(?P<pk>\d+)/$', views.detalhe_artigo, name='detalhe_artigo'),
    url(r'^artigo/novo/$', views.novo_artigo, name='novo_artigo'),
    url(r'^artigo/(?P<pk>\d+)/edicao/$', views.edicao_artigo, name='edicao_artigo'),
    url(r'^rascunhos/$', views.lista_rascunhos, name='lista_rascunhos'),
    url(r'^artigo/(?P<pk>\d+)/publicar/$',	views.publicar_artigo,	name='publicar_artigo'),
    url(r'^artigo/(?P<pk>\d+)/remover/$', views.remover_artigo, name='remover_artigo'),

    url(r'^termos/lista$', views.lista_termos, name='lista_termos'),
    url(r'^termos/(?P<pk>\d+)/$', views.detalhe_termos, name='detalhe_termos'),

    url(r'^farmacos/(?P<pk>\d+)/$', views.detalhe_farmacos, name='detalhe_farmacos'),
    url(r'^farmacos/lista$', views.lista_farmacos, name='lista_farmacos'),
]
