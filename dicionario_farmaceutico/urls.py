from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^farmacos/(?P<pk>\d+)/$', views.detalhe_farmacos, name='detalhe_farmacos'),
    url(r'^farmacos/lista$', views.lista_farmacos, name='lista_farmacos'),
]
