from django.db import models
from meajudaaajudar.models import Instituicao


class Donation(models.Model):
    time = models.DateTimeField(auto_created=True)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

    class Meta:
        db_table = "donation"
