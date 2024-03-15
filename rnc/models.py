from django.db import models


class DrRnc(models.Model):
    rnc = models.CharField(max_length=15, null=True)
    nombre = models.CharField(max_length=255, null=True)
    ocupacion = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
