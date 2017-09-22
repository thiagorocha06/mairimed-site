from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^mairimed/termos_uso/$', views.termos_uso, name='termos_uso'),
    url(r'^mairimed/sobre/$', views.sobre, name='sobre'),
    url(r'^mairimed/bootstrap/(?P<pk>\d+)/$', views.bootstrap, name='bootstrap'),

### ARTIGOS ###
    url(r'^artigo/infectologia/$', views.categorias_artigos, name='infectologia_artigos'),
    url(r'^artigo/cardiologia/$', views.categorias_artigos, name='cardiologia_artigos'),
    url(r'^artigo/endocrinologia/$', views.categorias_artigos, name='endocrinologia_artigos'),
    url(r'^artigo/nefrologia/$', views.categorias_artigos, name='nefrologia_artigos'),
    url(r'^artigo/pediatria/$', views.categorias_artigos, name='pediatria_artigos'),
    url(r'^artigo/pneumologia/$', views.categorias_artigos, name='pneumologia_artigos'),

    url(r'^artigo/(?P<pk>\d+)/$', views.detalhe_artigo, name='detalhe_artigo'),
    url(r'^artigo/(?P<pk>\d+)/favoritos/$', views.favoritos_artigo, name='favoritos_artigo'),

### ESCS ###
    url(r'^escs/1_serie/$', views.categorias_artigos, name='1_serie'),
    url(r'^escs/2_serie/$', views.categorias_artigos, name='2_serie'),
    url(r'^escs/3_serie/$', views.categorias_artigos, name='3_serie'),
    url(r'^escs/4_serie/$', views.categorias_artigos, name='4_serie'),

    url(r'^escs/M401/$', views.escs_artigos, name='M401'),
    url(r'^escs/M402/$', views.escs_artigos, name='M402'),
    url(r'^escs/M403/$', views.escs_artigos, name='M403'),
    url(r'^escs/M404/$', views.escs_artigos, name='M404'),
    url(r'^escs/M406/$', views.escs_artigos, name='M406'),
    url(r'^escs/M407/$', views.escs_artigos, name='M407'),
]
