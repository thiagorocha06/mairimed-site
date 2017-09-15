from django.contrib import admin
from artigos.models import Artigo, Termo, Farmaco

class ArtigoModelAdmin(admin.ModelAdmin):
    list_display = ["titulo", "data_de_criacao", "data_de_publicacao", "categoria", "modulo"]
    list_filter = ["categoria", "modulo"]
    search_fields = ["titulo"]
    class meta:
        model = Artigo

admin.site.register(Artigo, ArtigoModelAdmin)
admin.site.register(Farmaco)
admin.site.register(Termo)
