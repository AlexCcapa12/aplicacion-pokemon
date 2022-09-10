from django.db import models

class Owner(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.CharField(max_length=3)
    pais = models.CharField(max_length=20, default='')
    #description = models.TextField(max_length=500)

    def __str__(self):
        return "{} tiene {} años" .format(self.nombre, self.edad)



