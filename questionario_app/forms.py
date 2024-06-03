from django import forms 
from .models import Questao, Escolha

class QuestaoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QuestaoForm, self).__init__(*args, **kwargs)
        questoes = Questao.objects.all()
        for questao in questoes:
            escolhas = questao.escolhas.all()
            if escolhas:
                escolhas = [(escolha.id, escolha.text) for escolha in questao.escolhas.all()]
                self.fields[f'questao_{questao.id}'] = forms.ChoiceField(
                    choices=escolhas,
                    widget=forms.RadioSelect,
                    label=questao.text
                )
            else:
                self.fields[f'questao_{questao.id}'] = forms.CharField(
                    label=questao.text,
                )