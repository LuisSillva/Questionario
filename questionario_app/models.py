from django.db import models

# Create your models here.

# QUESTÕES
class Questao(models.Model):
    text = models.TextField(max_length=255)

    def __str__(self):
        return self.text

# ESCOLHAS DA QUESTÃO
class Escolha(models.Model):
    questao = models.ForeignKey(Questao, related_name='escolhas', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.text
    
# RESPOSTAS DO USUÁRIO
class Resposta(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    escolha = models.ForeignKey(Escolha, blank=True, null=True, on_delete=models.CASCADE)
    resposta_texto = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.resposta_texto if self.resposta_texto else f'{self.questao.text}: {self.escolha.text}'