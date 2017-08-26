from django.contrib import admin
from .models import Artigo

"""
from .models import Estudante

class EstudanteAdmin(admin.ModelAdmin):
    class Meta:
        model = Estudante

admin.site.register(Artigo, Estudante, EstudanteAdmin)
"""

admin.site.register(Artigo)
