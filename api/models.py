from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False, blank=False)
    image = models.ImageField()
