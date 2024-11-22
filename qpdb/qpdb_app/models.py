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
    
class Medley(models.Model):
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name} (Medley {self.id})"

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

class TuneMedleyRelationship(models.Model):
    def __str__(self):
        return f"{self.tune.name} in {self.medley.name}"

    def __repr__(self):
        return f"{self.tune.name} in {self.medley.name} (TuneMedleyRelationship {self.id})"

    class Meta:
        verbose_name = "Tune-Medley Relationship"

    tune = models.ForeignKey(
        Tune,
        on_delete=models.PROTECT,
    )
    medley = models.ForeignKey(
        Medley,
        on_delete=models.PROTECT,
    )
    position = models.IntegerField()

class MedleyPerformanceRelationship(models.Model):
    def __str__(self):
        return f"{self.medley.name} in {self.performance.name}"

    def __repr__(self):
        return f"{self.medley.name} in {self.performance.name} (MedleyPerformanceRelationship {self.id})"

    class Meta:
        verbose_name = "Medley-Performance Relationship"

    medley = models.ForeignKey(
        Medley,
        on_delete=models.PROTECT,
    )
    performance = models.ForeignKey(
        Performance,
        on_delete=models.PROTECT,
    )
    position = models.IntegerField()

