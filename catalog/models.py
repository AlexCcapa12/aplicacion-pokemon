from django.db import models

from django.db import models
from django.utils import timezone

class Catalogo(models.Model):
    nombre_catalogo = models.CharField(max_length=40)
    especie = models.CharField(max_length=20)
    genero = models.CharField(max_length=1)
    dia_creacion = models.DateTimeField(default=timezone.now())

# Create your models here.
