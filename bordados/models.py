from django.db import models


class Bordado(models.Model):
    nome = models.CharField(max_length=100)
    tamanho = models.CharField(max_length=10)
    quantidade = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=[
        ('Na Loja','Na Loja'),
        ('Bordando', 'Bordando'),
        ('Concluído', 'Concluído'),
    ])

    def __str__(self):
        return self.nome
