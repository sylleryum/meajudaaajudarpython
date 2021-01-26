from django.db import models


class Estado(models.Model):
    nome = models.CharField(max_length=200)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return '%s %s -- %s' % (self.id, self.nome, self.uf)

    class Meta:
        db_table = "estado"
