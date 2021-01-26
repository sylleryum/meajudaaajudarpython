from django.db import models


class Causa(models.Model):
    causa = models.CharField(max_length=200)

    # def __str__(self):
    #     return '%s %s -- %s %s' % (self.id, self.nome, self.estado.id, self.estado.nome)

    class Meta:
        db_table = "causa"

