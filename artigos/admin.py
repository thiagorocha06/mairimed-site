from django.contrib import admin
from artigos.models import Artigo, Termo, Farmaco

admin.site.register(Artigo)
admin.site.register(Farmaco)
admin.site.register(Termo)
