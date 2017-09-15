from django.conf.urls import url
from . import views

urlpatterns = [

### TERMOS ###
    url(r'^termos/(?P<pk>\d+)/$', views.detalhe_termos, name='detalhe_termos'),
    url(r'^termos/lista$', views.lista_termos, name='lista_termos'),
]
