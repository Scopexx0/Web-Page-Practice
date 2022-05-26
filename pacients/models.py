from django.db import models

# Create your models here.

class Pacient(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    dni = models.IntegerField()
