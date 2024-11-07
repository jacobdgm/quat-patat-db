from django.db import models

class Tune(models.Model):
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name} ({self.id})"

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
    
