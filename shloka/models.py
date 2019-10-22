from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Rapper(models.Model):
    name = models.CharField(max_length=150)
    stage_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=10,validators=[RegexValidator(r'^[6-9]{1}[0-9]{9}$')])
    instagram = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Audience(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=10,validators=[RegexValidator(r'^[6-9]{1}[0-9]{9}$')])
    instagram = models.CharField(max_length=50)
    three_rappers = models.CharField(max_length=100)
    three_songs = models.CharField(max_length=100)
    three_rap_songs = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    