from django.db import models

class Usuario(models.Model):
    nombre_usuario=models.CharField(max_length=15)
    nombre=models.CharField(max_length=15)
    apellido=models.CharField(max_length=15)
    edad=models.IntegerField(max_length=15)
# Create your models here.
