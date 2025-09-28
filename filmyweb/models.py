from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    rok = models.PositiveIntegerField(default=2000)