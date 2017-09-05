from django import forms
from .models import Artigo

class ArtigoForm(forms.ModelForm):

    class Meta:
        model = Artigo
        fields = (
        'titulo', 'introducao', 'epidemiologia',
        'etiologia_fisiopatologia', 'diagnostico',
        'historia_clinica', 'exames_complementares',
        'criterios_diagnosticos', 'diagnostico_diferencial',
        'tratamento_e_manejo', 'prognostico', 'complicacoes'
        )
