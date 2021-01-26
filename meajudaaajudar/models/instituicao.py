from django.db import models
from meajudaaajudar.models import Cidade
from meajudaaajudar.models import Causa
from meajudaaajudar.models import Contato


class Instituicao(models.Model):
    causa = models.ForeignKey(Causa, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    contato = models.OneToOneField(Contato, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=2000, null=True)
    doar_link = models.CharField(max_length=255, null=True)
    imagem = models.CharField(max_length=500, null=True)
    nome = models.CharField(max_length=255, null=True)
    sobre = models.CharField(max_length=4000, null=True)
    url = models.CharField(max_length=255, null=True)
    info_doacao = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "instituicao"
