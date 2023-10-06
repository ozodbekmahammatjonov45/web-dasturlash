from django.db import models

class Lugat(models.Model):

    inglizcha = models.CharField('inglizcha', max_length=400)
    uzbekcha = models.CharField('uzbekcha', max_length=400)

