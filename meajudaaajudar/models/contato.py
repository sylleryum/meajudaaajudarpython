from django.db import models
from meajudaaajudar.models import Cidade


class Contato(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=200, null=True)
    numero = models.CharField(max_length=200, null=True)
    telefone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    # def __str__(self):
    #     return '%s %s -- %s %s' % (self.id, self.nome, self.estado.id, self.estado.nome)

    class Meta:
        db_table = "contato"

