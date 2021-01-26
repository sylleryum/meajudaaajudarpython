from django.db import models


class ApiUser(models.Model):
    password = models.CharField(max_length=500)
    role = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    # def __str__(self):
    #     return '%s %s -- %s %s' % (self.id, self.nome, self.estado.id, self.estado.nome)

    class Meta:
        db_table = "api_user"

