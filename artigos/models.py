from django.db import models
from django.utils import timezone

class Artigo(models.Model):
    author = models.ForeignKey('auth.User')
    data_de_criacao = models.DateTimeField(default=timezone.now)
    data_de_publicacao = models.DateTimeField(blank=True, null=True)
    categoria = models.CharField(max_length=200, blank=True, null=True)
    titulo = models.CharField(max_length=200)
    introducao = models.TextField(blank=True)
    epidemiologia = models.TextField(blank=True)
    etiologia_fisiopatologia = models.TextField(blank=True)
    diagnostico = models.TextField(blank=True)
    historia_clinica = models.TextField(blank=True)
    exames_complementares = models.TextField(blank=True)
    criterios_diagnosticos = models.TextField(blank=True)
    diagnostico_diferencial = models.TextField(blank=True)
    tratamento_e_manejo = models.TextField(blank=True)
    prognostico = models.TextField(blank=True)
    complicacoes = models.TextField(blank=True)
    referencias = models.TextField(blank=True)

    def publicar(self):
        self.data_de_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Termo(models.Model):
    nome = models.CharField(max_length=50)
    origem = models.CharField(max_length=50)
    definicao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Farmaco(models.Model):
    nome = models.CharField(max_length=50)
    classe = models.CharField(max_length=50)
    subclasse = models.CharField(max_length=50)
    marcas = models.CharField(max_length=50)
    farmacodinamica = models.CharField(max_length=50)
    farmacocinetica = models.CharField(max_length=50)
    absorcao = models.CharField(max_length=50)
    distribuicao = models.CharField(max_length=50)
    metabolismo = models.CharField(max_length=50)
    eliminacao = models.CharField(max_length=50)
    indicacoes = models.CharField(max_length=50)
    posologia = models.CharField(max_length=50)
    pediatria = models.CharField(max_length=50)
    administracao = models.CharField(max_length=50)
    rmuitocomum = models.CharField(max_length=50)
    rcomum = models.CharField(max_length=50)
    rincomum = models.CharField(max_length=50)
    rrara = models.CharField(max_length=50)
    rmuitorara = models.CharField(max_length=50)
    rnaodefinida = models.CharField(max_length=50)
    alteracaoexames = models.CharField(max_length=50)
    contraindicacoes = models.CharField(max_length=50)
    gravidez = models.CharField(max_length=50)
    lactacao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
