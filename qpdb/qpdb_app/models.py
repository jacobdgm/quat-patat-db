from django.db import models

class Tune(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
    )
    type = models.CharField(
        max_length=255,
        blank=True,
    )
    key = models.CharField(
        max_length=255,
        blank=True,
    )
    composer = models.CharField(
        max_length=255,
        blank=True,
    )
    notes = models.TextField(
        blank=True,
    )
    
