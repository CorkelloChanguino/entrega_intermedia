from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    numero_dia = models.IntegerField()


class Profesores(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    cantidad_dia = models.IntegerField()


class Materias(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    cantidad_dia = models.IntegerField()
