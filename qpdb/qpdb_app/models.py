from django.db import models

class Tune(models.Model):
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name} (Tune {self.id})"

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
    
class Set(models.Model):
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name} (Set {self.id})"

    name = models.CharField(
        max_length=255,
        blank=False,
    )
    type = models.CharField(
        max_length=255,
        blank=True,
    )
    notes = models.TextField(
        blank=True,
    )

class Performance(models.Model):
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name} (Performance {self.id})"

    name = models.CharField(
        max_length=255,
        blank=False,
    )
    type = models.CharField(
        max_length=255,
        blank=True,
    )
    notes = models.TextField(
        blank=True,
    )
    date = models.DateTimeField(
        blank=True,
    )

