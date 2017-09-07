from django import forms
from .models import Artigo

class ArtigoForm(forms.ModelForm):

    class Meta:
        model = Artigo
        fields = (
        'modulo', 'categoria',
        'titulo', 'introducao', 'intro_figura', 'epidemiologia',
        'etiologia_fisiopatologia', 'diagnostico',
        'historia_clinica', 'exame_fisico', 'exames_complementares',
        'criterios_diagnosticos', 'diagnostico_diferencial',
        'tratamento_e_manejo', 'tratamento_nao_medicamentoso',
        'tratamento_medicamentoso', 'tratamento_intervencionista',
        'profilaxia', 'prognostico', 'complicacoes', 'algoritmo', 'referencias'
        )
