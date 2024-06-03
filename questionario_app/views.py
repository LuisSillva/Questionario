from django.shortcuts import render, redirect
from .models import Questao, Escolha, Resposta
from .forms import QuestaoForm
from django.views import View
from django.db.models import Count

# Create your views here.

class HomeView(View):
    def get(self, request):
        form = QuestaoForm()
        return render(request, 'home.html', {'form': form})
    
    def post(self, request):
        form = QuestaoForm(request.POST)
        if form.is_valid():
            for key, value in form.cleaned_data.items():
                questao_id = key.split('_')[1]
                questao = Questao.objects.get(id=questao_id)
                if isinstance(value, str):
                    resposta_texto = value
                    escolha = None
                else:

                    escolha = Escolha.objects.get(id=value)
                    resposta_texto = None
                Resposta.objects.create(questao=questao, escolha=escolha, resposta_texto=resposta_texto)

            return redirect('results')
        return render(request, 'home.html', {'form': form})

class ResultsView(View):
    def get(self, request):
        questoes = Questao.objects.all()
        data = []
        for questao in questoes:
            escolhas = Escolha.objects.filter(questao=questao).annotate(vote_count=Count('resposta'))
            if escolhas.exists():
                data.append({
                    'questao': questao,
                    'escolhas': escolhas
                })
            else:
                respostas_livres = Resposta.objects.filter(questao=questao).exclude(resposta_texto='')
                data.append({
                    'questao': questao,
                    'respostas_livres': respostas_livres
                })
        print(data)
        return render(request, 'results.html', {'data': data})

