from django.db import models
from django.utils import timezone

# Create your models here.

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_de_publicacao = models.DateTimeField(blank=True, null=True)
    #favoritos = models.IntegerField()

    def publicar(self):
        self.data_pub = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
