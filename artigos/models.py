from django.db import models
from django.utils import timezone
from django.conf import settings

class Artigo(models.Model):
    author = models.ForeignKey('auth.User')
    data_de_criacao = models.DateTimeField(default=timezone.now)
    data_de_publicacao = models.DateTimeField(blank=True, null=True)
    modulo = models.CharField(max_length=200, blank=True, null=True)
    categoria = models.CharField(max_length=200, blank=True, null=True)
    titulo = models.CharField(max_length=200)
    introducao = models.TextField(blank=True, null=True)
    intro_figura = models.ImageField(upload_to='img', blank=True, null=True)
    epidemiologia = models.TextField(blank=True, null=True)
    epidemio_figura = models.ImageField(upload_to='img', blank=True, null=True)
    classificacao = models.TextField(blank=True, null=True)
    clas_figura = models.ImageField(upload_to='img', blank=True, null=True)

    etiologia_fisiopatologia = models.TextField(blank=True, null=True)
    etio_top1 = models.TextField(blank=True, null=True)
    etio_texto1 = models.TextField(blank=True, null=True)
    etio_top2 = models.TextField(blank=True, null=True)
    etio_texto2 = models.TextField(blank=True, null=True)
    etio_top3 = models.TextField(blank=True, null=True)
    etio_texto3 = models.TextField(blank=True, null=True)
    etio_top4 = models.TextField(blank=True, null=True)
    etio_texto4 = models.TextField(blank=True, null=True)
    etio_top5 = models.TextField(blank=True, null=True)
    etio_texto5 = models.TextField(blank=True, null=True)
    etio_top6 = models.TextField(blank=True, null=True)
    etio_texto6 = models.TextField(blank=True, null=True)
    etio_figura = models.ImageField(upload_to='img', blank=True, null=True)

    diagnostico = models.TextField(blank=True, null=True)
    historia_clinica = models.TextField(blank=True, null=True)
    historia_figura = models.ImageField(upload_to='img', blank=True, null=True)
    exame_fisico = models.TextField(blank=True, null=True)
    ef_top1 = models.TextField(blank=True, null=True)
    ef_texto1 = models.TextField(blank=True, null=True)
    ef_top2 = models.TextField(blank=True, null=True)
    ef_texto2 = models.TextField(blank=True, null=True)
    ef_top3 = models.TextField(blank=True, null=True)
    ef_texto3 = models.TextField(blank=True, null=True)
    ef_top4 = models.TextField(blank=True, null=True)
    ef_texto4 = models.TextField(blank=True, null=True)
    exames_complementares = models.TextField(blank=True, null=True)
    exames_top1 = models.TextField(blank=True, null=True)
    exames_texto1 = models.TextField(blank=True, null=True)
    exames_top2 = models.TextField(blank=True, null=True)
    exames_texto2 = models.TextField(blank=True, null=True)
    exames_top3 = models.TextField(blank=True, null=True)
    exames_texto3 = models.TextField(blank=True, null=True)
    exames_top4 = models.TextField(blank=True, null=True)
    exames_texto4 = models.TextField(blank=True, null=True)
    exames_top5 = models.TextField(blank=True, null=True)
    exames_texto5 = models.TextField(blank=True, null=True)
    exames_top6 = models.TextField(blank=True, null=True)
    exames_texto6 = models.TextField(blank=True, null=True)
    criterios_diagnosticos = models.TextField(blank=True, null=True)
    diagnostico_diferencial = models.TextField(blank=True, null=True)
    diag_figura = models.ImageField(upload_to='img', blank=True, null=True)

    top1 = models.TextField(blank=True, null=True)
    texto1 = models.TextField(blank=True, null=True)
    top1_img1 = models.ImageField(upload_to='img', blank=True, null=True)
    top1_img2 = models.ImageField(upload_to='img', blank=True, null=True)

    tratamento_e_manejo = models.TextField(blank=True, null=True)
    tratamento_nao_medicamentoso = models.TextField(blank=True, null=True)
    tratamento_medicamentoso = models.TextField(blank=True, null=True)
    med_top1 = models.TextField(blank=True, null=True)
    med_texto1 = models.TextField(blank=True, null=True)
    med_top2 = models.TextField(blank=True, null=True)
    med_texto2 = models.TextField(blank=True, null=True)
    med_top3 = models.TextField(blank=True, null=True)
    med_texto3 = models.TextField(blank=True, null=True)
    med_top4 = models.TextField(blank=True, null=True)
    med_texto4 = models.TextField(blank=True, null=True)
    med_top5 = models.TextField(blank=True, null=True)
    med_texto5 = models.TextField(blank=True, null=True)
    med_top6 = models.TextField(blank=True, null=True)
    med_texto6 = models.TextField(blank=True, null=True)
    tratamento_intervencionista = models.TextField(blank=True, null=True)
    trat_figura = models.ImageField(upload_to='img', blank=True, null=True)
    profilaxia = models.TextField(blank=True, null=True)
    prof_figura = models.ImageField(upload_to='img', blank=True, null=True)
    prognostico = models.TextField(blank=True, null=True)
    complicacoes = models.TextField(blank=True, null=True)
    algoritmo = models.ImageField(upload_to='img', blank=True, null=True)
    referencias = models.TextField(blank=True, null=True)

    def publicar(self):
        self.data_de_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Termo(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    origem = models.TextField(max_length=50, blank=True, null=True)
    definicao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Farmaco(models.Model):
    nome = models.TextField(max_length=50, blank=True, null=True)
    classe = models.TextField(blank=True, null=True)
    subclasse = models.TextField(blank=True, null=True)
    marcas = models.TextField(blank=True, null=True)
    farmacodinamica = models.TextField(blank=True, null=True)
    farmacocinetica = models.TextField(blank=True, null=True)
    absorcao = models.TextField(blank=True, null=True)
    distribuicao = models.TextField(blank=True, null=True)
    metabolismo = models.TextField(blank=True, null=True)
    eliminacao = models.TextField(blank=True, null=True)
    indicacoes = models.TextField(blank=True, null=True)
    posologia = models.TextField(blank=True, null=True)
    pediatria = models.TextField(blank=True, null=True)
    administracao = models.TextField(blank=True, null=True)
    rmuitocomum = models.TextField(blank=True, null=True)
    rcomum = models.TextField(blank=True, null=True)
    rincomum = models.TextField(blank=True, null=True)
    rrara = models.TextField(blank=True, null=True)
    rmuitorara = models.TextField(blank=True, null=True)
    rnaodefinida = models.TextField(blank=True, null=True)
    alteracaoexames = models.TextField(blank=True, null=True)
    contraindicacoes = models.TextField(blank=True, null=True)
    gravidez = models.TextField(blank=True, null=True)
    lactacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Exercicio(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.CharField(max_length=200, blank=True, null=True)
    exercicio_img = models.ImageField(upload_to='img', blank=True, null=True)
    exercicio_historia = models.TextField(blank=True, null=True)
    exercicio_resposta = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
