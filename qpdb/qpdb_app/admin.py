from django.contrib import admin
from .models import (
    Tune,
    Set,
    Performance,
    TuneSetRelationship,
    SetPerformanceRelationship,
)

admin.site.register(Tune)
admin.site.register(Set)
admin.site.register(Performance)
admin.site.register(TuneSetRelationship)
admin.site.register(SetPerformanceRelationship)

