from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lista_artigos, name='lista_artigos'),
    url(r'^artigo/(?P<pk>\d+)/$', views.detalhe_artigo, name='detalhe_artigo'),
    url(r'^artigo/novo/$', views.novo_artigo, name='novo_artigo'),
    url(r'^artigo/(?P<pk>\d+)/edicao/$', views.edicao_artigo, name='edicao_artigo'),
    url(r'^rascunhos/$', views.lista_rascunhos, name='lista_rascunhos'),
    url(r'^artigo/(?P<pk>\d+)/publicar/$',	views.publicar_artigo,	name='publicar_artigo'),
    url(r'^artigo/(?P<pk>\d+)/remover/$', views.remover_artigo, name='remover_artigo'),
]
