from django.db import models
from django.forms import DateInput

# Create your models here.

class Turns(models.Model):
    day = models.DateField()