from django.db import models

# Create your models here.
# countries/models.py


class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    area = models.IntegerField(help_text="(in square kilometers)")
