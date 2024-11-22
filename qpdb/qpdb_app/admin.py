from django.contrib import admin
from .models import (
    Tune,
    Medley,
    Performance,
    TuneMedleyRelationship,
    MedleyPerformanceRelationship,
)

admin.site.register(Tune)
admin.site.register(Medley)
admin.site.register(Performance)
admin.site.register(TuneMedleyRelationship)
admin.site.register(MedleyPerformanceRelationship)

