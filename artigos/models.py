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

    intro_top = models.CharField(max_length=200, blank=True, null=True, default="INTRODUÇÃO")
    introducao = models.TextField(blank=True, null=True)
    intro_top1 = models.CharField(max_length=200, blank=True, null=True)
    intro_texto1 = models.TextField(blank=True, null=True)
    intro_top2 = models.CharField(max_length=200, blank=True, null=True)
    intro_texto2 = models.TextField(blank=True, null=True)
    intro_top3 = models.CharField(max_length=200, blank=True, null=True)
    intro_texto3 = models.TextField(blank=True, null=True)
    intro_top4 = models.CharField(max_length=200, blank=True, null=True)
    intro_texto4 = models.TextField(blank=True, null=True)
    intro_top5 = models.CharField(max_length=200, blank=True, null=True)
    intro_texto5 = models.TextField(blank=True, null=True)
    intro_top6 = models.CharField(max_length=200, blank=True, null=True)
    intro_texto6 = models.TextField(blank=True, null=True)
    intro_figura1 = models.ImageField(upload_to='img', blank=True, null=True)
    intro_figura2 = models.ImageField(upload_to='img', blank=True, null=True)

    epidemio_top = models.CharField(max_length=200, blank=True, null=True, default="EPIDEMIOLOGIA")
    epidemiologia = models.TextField(blank=True, null=True)
    epidemio_top1 = models.CharField(max_length=200, blank=True, null=True)
    epidemio_texto1 = models.TextField(blank=True, null=True)
    epidemio_top2 = models.CharField(max_length=200, blank=True, null=True)
    epidemio_texto2 = models.TextField(blank=True, null=True)
    epidemio_top3 = models.CharField(max_length=200, blank=True, null=True)
    epidemio_texto3 = models.TextField(blank=True, null=True)
    epidemio_top4 = models.CharField(max_length=200, blank=True, null=True)
    epidemio_texto4 = models.TextField(blank=True, null=True)
    epidemio_top5 = models.CharField(max_length=200, blank=True, null=True)
    epidemio_texto5 = models.TextField(blank=True, null=True)
    epidemio_figura = models.ImageField(upload_to='img', blank=True, null=True)

    class_top = models.CharField(max_length=200, blank=True, null=True, default="CLASSIFICAÇÃO")
    classificacao = models.TextField(blank=True, null=True)
    class_top1 = models.CharField(max_length=200, blank=True, null=True)
    class_texto1 = models.TextField(blank=True, null=True)
    class_top2 = models.CharField(max_length=200, blank=True, null=True)
    class_texto2 = models.TextField(blank=True, null=True)
    class_top3 = models.CharField(max_length=200, blank=True, null=True)
    class_texto3 = models.TextField(blank=True, null=True)
    class_top4 = models.CharField(max_length=200, blank=True, null=True)
    class_texto4 = models.TextField(blank=True, null=True)
    class_top5 = models.CharField(max_length=200, blank=True, null=True)
    class_texto5 = models.TextField(blank=True, null=True)
    clas_figura = models.ImageField(upload_to='img', blank=True, null=True)

    etio_top = models.CharField(max_length=200, blank=True, null=True, default="ETIOLOGIA E FISIOPATOLOGIA")
    etiologia_fisiopatologia = models.TextField(blank=True, null=True)
    etio_top1 = models.CharField(max_length=200, blank=True, null=True)
    etio_texto1 = models.TextField(blank=True, null=True)
    etio_top2 = models.CharField(max_length=200, blank=True, null=True)
    etio_texto2 = models.TextField(blank=True, null=True)
    etio_top3 = models.CharField(max_length=200, blank=True, null=True)
    etio_texto3 = models.TextField(blank=True, null=True)
    etio_top4 = models.CharField(max_length=200, blank=True, null=True)
    etio_texto4 = models.TextField(blank=True, null=True)
    etio_top5 = models.CharField(max_length=200, blank=True, null=True)
    etio_texto5 = models.TextField(blank=True, null=True)
    etio_top6 = models.CharField(max_length=200, blank=True, null=True)
    etio_texto6 = models.TextField(blank=True, null=True)
    etio_top7 = models.CharField(max_length=200, blank=True, null=True)
    etio_texto7 = models.TextField(blank=True, null=True)
    etio_top8 = models.CharField(max_length=200, blank=True, null=True)
    etio_texto8 = models.TextField(blank=True, null=True)
    etio_img1 = models.ImageField(upload_to='img', blank=True, null=True)
    etio_img2 = models.ImageField(upload_to='img', blank=True, null=True)

    diag_top = models.CharField(max_length=200, blank=True, null=True, default="DIAGNÓSTICO")
    diagnostico = models.TextField(blank=True, null=True)

    historia_top = models.CharField(max_length=200, blank=True, null=True, default="HISTÓRIA CLÍNICA")
    historia_clinica = models.TextField(blank=True, null=True)
    historia_top1 = models.CharField(max_length=200, blank=True, null=True)
    historia_texto1 = models.TextField(blank=True, null=True)
    historia_top2 = models.CharField(max_length=200, blank=True, null=True)
    historia_texto2 = models.TextField(blank=True, null=True)
    historia_top3 = models.CharField(max_length=200, blank=True, null=True)
    historia_texto3 = models.TextField(blank=True, null=True)
    historia_top4 = models.CharField(max_length=200, blank=True, null=True)
    historia_texto4 = models.TextField(blank=True, null=True)
    historia_top5 = models.CharField(max_length=200, blank=True, null=True)
    historia_texto5 = models.TextField(blank=True, null=True)
    historia_top6 = models.CharField(max_length=200, blank=True, null=True)
    historia_texto6 = models.TextField(blank=True, null=True)
    historia_figura = models.ImageField(upload_to='img', blank=True, null=True)

    ef_top = models.CharField(max_length=200, blank=True, null=True, default="EXAME FÍSICO")
    exame_fisico = models.TextField(blank=True, null=True)
    ef_top1 = models.CharField(max_length=200, blank=True, null=True)
    ef_texto1 = models.TextField(blank=True, null=True)
    ef_top2 = models.CharField(max_length=200, blank=True, null=True)
    ef_texto2 = models.TextField(blank=True, null=True)
    ef_top3 = models.CharField(max_length=200, blank=True, null=True)
    ef_texto3 = models.TextField(blank=True, null=True)
    ef_top4 = models.CharField(max_length=200, blank=True, null=True)
    ef_texto4 = models.TextField(blank=True, null=True)
    ef_top5 = models.CharField(max_length=200, blank=True, null=True)
    ef_texto5 = models.TextField(blank=True, null=True)
    ef_top6 = models.CharField(max_length=200, blank=True, null=True)
    ef_texto6 = models.TextField(blank=True, null=True)
    ef_figura = models.ImageField(upload_to='img', blank=True, null=True)

    exames_top = models.CharField(max_length=200, blank=True, null=True, default="EXAMES COMPLEMENTARES")
    exames_complementares = models.TextField(blank=True, null=True)
    exames_top1 = models.CharField(max_length=200, blank=True, null=True)
    exames_texto1 = models.TextField(blank=True, null=True)
    exames_top2 = models.CharField(max_length=200, blank=True, null=True)
    exames_texto2 = models.TextField(blank=True, null=True)
    exames_top3 = models.CharField(max_length=200, blank=True, null=True)
    exames_texto3 = models.TextField(blank=True, null=True)
    exames_top4 = models.CharField(max_length=200, blank=True, null=True)
    exames_texto4 = models.TextField(blank=True, null=True)
    exames_top5 = models.CharField(max_length=200, blank=True, null=True)
    exames_texto5 = models.TextField(blank=True, null=True)
    exames_top6 = models.CharField(max_length=200, blank=True, null=True)
    exames_texto6 = models.TextField(blank=True, null=True)
    exames_img1 = models.ImageField(upload_to='img', blank=True, null=True)
    exames_img2 = models.ImageField(upload_to='img', blank=True, null=True)
    exames_img3 = models.ImageField(upload_to='img', blank=True, null=True)
    criterios_top = models.CharField(max_length=200, blank=True, null=True, default="CRITÉRIOS DIAGNÓSTICOS")
    criterios_diagnosticos = models.TextField(blank=True, null=True)
    dd_top = models.CharField(max_length=200, blank=True, null=True, default="DIAGNÓSTICO DIFERENCIAL")
    diagnostico_diferencial = models.TextField(blank=True, null=True)
    diag_figura = models.ImageField(upload_to='img', blank=True, null=True)

    top1 = models.CharField(max_length=200, blank=True, null=True)
    texto1 = models.TextField(blank=True, null=True)
    subtop1 = models.CharField(max_length=200, blank=True, null=True)
    subtexto1 = models.TextField(blank=True, null=True)
    subtop2 = models.CharField(max_length=200, blank=True, null=True)
    subtexto2 = models.TextField(blank=True, null=True)
    subtop3 = models.CharField(max_length=200, blank=True, null=True)
    subtexto3 = models.TextField(blank=True, null=True)
    subtop4 = models.CharField(max_length=200, blank=True, null=True)
    subtexto4 = models.TextField(blank=True, null=True)
    subtop5 = models.CharField(max_length=200, blank=True, null=True)
    subtexto5 = models.TextField(blank=True, null=True)
    subtop6 = models.CharField(max_length=200, blank=True, null=True)
    subtexto6 = models.TextField(blank=True, null=True)
    top1_img1 = models.ImageField(upload_to='img', blank=True, null=True)
    top1_img2 = models.ImageField(upload_to='img', blank=True, null=True)

    tratamento_top = models.CharField(max_length=200, blank=True, null=True, default="TRATAMENTO E MANEJO")
    tratamento_e_manejo = models.TextField(blank=True, null=True)
    medidas_top = models.CharField(max_length=200, blank=True, null=True, default="MEDIDAS GERAIS")
    tratamento_nao_medicamentoso = models.TextField(blank=True, null=True)
    medidas_top1 = models.CharField(max_length=200, blank=True, null=True)
    medidas_texto1 = models.TextField(blank=True, null=True)
    medidas_top2 = models.CharField(max_length=200, blank=True, null=True)
    medidas_texto2 = models.TextField(blank=True, null=True)
    medidas_top3 = models.CharField(max_length=200, blank=True, null=True)
    medidas_texto3 = models.TextField(blank=True, null=True)
    medidas_top4 = models.CharField(max_length=200, blank=True, null=True)
    medidas_texto4 = models.TextField(blank=True, null=True)
    medidas_top5 = models.CharField(max_length=200, blank=True, null=True)
    medidas_texto5 = models.TextField(blank=True, null=True)
    medidas_top6 = models.CharField(max_length=200, blank=True, null=True)
    medidas_texto6 = models.TextField(blank=True, null=True)

    trat_med_top = models.CharField(max_length=200, blank=True, null=True, default="TRATAMENTO FARMACOLÓGICO")
    tratamento_medicamentoso = models.TextField(blank=True, null=True)
    med_top1 = models.CharField(max_length=200, blank=True, null=True)
    med_texto1 = models.TextField(blank=True, null=True)
    med_top2 = models.CharField(max_length=200, blank=True, null=True)
    med_texto2 = models.TextField(blank=True, null=True)
    med_top3 = models.CharField(max_length=200, blank=True, null=True)
    med_texto3 = models.TextField(blank=True, null=True)
    med_top4 = models.CharField(max_length=200, blank=True, null=True)
    med_texto4 = models.TextField(blank=True, null=True)
    med_top5 = models.CharField(max_length=200, blank=True, null=True)
    med_texto5 = models.TextField(blank=True, null=True)
    med_top6 = models.CharField(max_length=200, blank=True, null=True)
    med_texto6 = models.TextField(blank=True, null=True)
    med_top7 = models.CharField(max_length=200, blank=True, null=True)
    med_texto7 = models.TextField(blank=True, null=True)
    med_top8 = models.CharField(max_length=200, blank=True, null=True)
    med_texto8 = models.TextField(blank=True, null=True)

    trat_int_top = models.CharField(max_length=200, blank=True, null=True, default="TRATAMENTO INTERVENCIONISTA")
    tratamento_intervencionista = models.TextField(blank=True, null=True)
    trat_int_top1 = models.CharField(max_length=200, blank=True, null=True)
    trat_int_texto1 = models.TextField(blank=True, null=True)
    trat_int_top2 = models.CharField(max_length=200, blank=True, null=True)
    trat_int_texto2 = models.TextField(blank=True, null=True)
    trat_int_top3 = models.CharField(max_length=200, blank=True, null=True)
    trat_int_texto3 = models.TextField(blank=True, null=True)
    trat_int_top4 = models.CharField(max_length=200, blank=True, null=True)
    trat_int_texto4 = models.TextField(blank=True, null=True)
    trat_figura = models.ImageField(upload_to='img', blank=True, null=True)

    profilaxia_top = models.CharField(max_length=200, blank=True, null=True, default="PROFILAXIA")
    profilaxia = models.TextField(blank=True, null=True)
    profilaxia_top1 = models.CharField(max_length=200, blank=True, null=True)
    profilaxia_texto1 = models.TextField(blank=True, null=True)
    profilaxia_top2 = models.CharField(max_length=200, blank=True, null=True)
    profilaxia_texto2 = models.TextField(blank=True, null=True)
    profilaxia_top3 = models.CharField(max_length=200, blank=True, null=True)
    profilaxia_texto3 = models.TextField(blank=True, null=True)
    profilaxia_top4 = models.CharField(max_length=200, blank=True, null=True)
    profilaxia_texto4 = models.TextField(blank=True, null=True)
    profilaxia_top5 = models.CharField(max_length=200, blank=True, null=True)
    profilaxia_texto5 = models.TextField(blank=True, null=True)
    profilaxia_top6 = models.CharField(max_length=200, blank=True, null=True)
    profilaxia_texto6 = models.TextField(blank=True, null=True)
    prof_figura = models.ImageField(upload_to='img', blank=True, null=True)

    prognostico_top = models.CharField(max_length=200, blank=True, null=True, default="PROGNÓSTICO")
    prognostico = models.TextField(blank=True, null=True)
    prognostico_img = models.ImageField(upload_to='img', blank=True, null=True)
    complicacoes_top = models.CharField(max_length=200, blank=True, null=True, default="COMPLICAÇÕES")
    complicacoes = models.TextField(blank=True, null=True)
    algoritmo_top = models.CharField(max_length=200, blank=True, null=True, default="ALGORITMO")
    algoritmo_img1 = models.ImageField(upload_to='img', blank=True, null=True)
    algoritmo_img2 = models.ImageField(upload_to='img', blank=True, null=True)
    algoritmo_img3 = models.ImageField(upload_to='img', blank=True, null=True)
    referencias_top = models.CharField(max_length=200, blank=True, null=True, default="REFERENCIAS")
    referencias = models.TextField(blank=True, null=True)

    def publicar(self):
        self.data_de_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
