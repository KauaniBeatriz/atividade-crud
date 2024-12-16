from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)
    profissao = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True, default='00000000000')  # Adicionando o valor padrão


    def __str__(self):
        return self.nome
