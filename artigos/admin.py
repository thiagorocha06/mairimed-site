from django.contrib import admin
from artigos.models import Artigo, Termo, Farmaco, Exercicio

admin.site.register(Artigo)
admin.site.register(Farmaco)
admin.site.register(Termo)
admin.site.register(Exercicio)
