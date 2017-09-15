from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),

### TERMOS ###
    url(r'^termos/(?P<pk>\d+)/$', views.detalhe_termos, name='detalhe_termos'),
    url(r'^termos/lista$', views.lista_termos, name='lista_termos'),

### FARMACOS ###
    url(r'^farmacos/(?P<pk>\d+)/$', views.detalhe_farmacos, name='detalhe_farmacos'),
    url(r'^farmacos/lista$', views.lista_farmacos, name='lista_farmacos'),

### ARTIGOS ###
    url(r'^artigo/categorias/$', views.categorias_artigos, name='categorias_artigos'),
    url(r'^artigo/infectologia/$', views.infectologia_artigos, name='infectologia_artigos'),
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

    url(r'^artigo/(?P<pk>\d+)/favoritos/$', views.favoritos_artigo, name='favoritos_artigo'),
    #url(r'^artigo/pesquisa/$', views.pesquisa_artigos, name='pesquisa_artigos'),

### ESCS ###
    url(r'^escs/1_serie/$', views.p_serie, name='1_serie'),
    url(r'^escs/2_serie/$', views.s_serie, name='2_serie'),
    url(r'^escs/3_serie/$', views.t_serie, name='3_serie'),
    url(r'^escs/4_serie/$', views.q_serie, name='4_serie'),

    url(r'^escs/M401/$', views.M401, name='M401'),
    url(r'^escs/M402/$', views.M402, name='M402'),
    url(r'^escs/M403/$', views.M403, name='M403'),
    url(r'^escs/M404/$', views.M404, name='M404'),
    url(r'^escs/M406/$', views.M406, name='M406'),
    url(r'^escs/M407/$', views.M407, name='M407'),
]
