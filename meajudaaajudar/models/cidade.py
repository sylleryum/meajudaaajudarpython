from django.db import models
from meajudaaajudar.models import Estado


class Cidade(models.Model):
    nome = models.CharField(max_length=200)
    estado = models.ForeignKey(
        Estado,
        related_name='cidade',
        on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s -- %s %s' % (self.id, self.nome, self.estado.id, self.estado.nome)

    class Meta:
        db_table = "cidade"
