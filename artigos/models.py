from django.db import models
from django.utils import timezone

class Artigo(models.Model):
    author = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_de_criacao = models.DateTimeField(default=timezone.now)
    data_de_publicacao = models.DateTimeField(blank=True, null=True)
    #favoritos = models.IntegerField()

    def publicar(self):
        self.data_de_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class DicioMed(models.Model):
    nome = models.CharField(max_length=50)
    origem = models.CharField(max_length=50)
    definicao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
