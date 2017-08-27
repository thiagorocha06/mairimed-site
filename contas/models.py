from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Estudante(models.Model):
    nome = models.OneToOneField(User)
    instituicao = models.CharField(max_length=30, default='')
    semestre = models.CharField(max_length=10, default='')

def criar_estudante(sender, **kwargs):
    if kwargs['created']:
        estudante = Estudante.objects.create(nome=kwargs['instance'])

post_save.connect(criar_estudante, sender=User)