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

class TuneSetRelationship(models.Model):
    def __str__(self):
        return f"{self.tune.name} in {self.set.name}"

    def __repr__(self):
        return f"{self.tune.name} in {self.set.name} (TuneSetRelationship {self.id})"

    class Meta:
        verbose_name = "Tune-Set Relationship"

    tune = models.ForeignKey(
        Tune,
        on_delete=models.PROTECT,
    )
    set = models.ForeignKey(
        Set,
        on_delete=models.PROTECT,
    )
    position = models.IntegerField()

class SetPerformanceRelationship(models.Model):
    def __str__(self):
        return f"{self.set.name} in {self.performance.name}"

    def __repr__(self):
        return f"{self.set.name} in {self.performance.name} (SetPerformanceRelationship {self.id})"

    class Meta:
        verbose_name = "Set-Performance Relationship"

    set = models.ForeignKey(
        Set,
        on_delete=models.PROTECT,
    )
    performance = models.ForeignKey(
        Performance,
        on_delete=models.PROTECT,
    )
    position = models.IntegerField()

