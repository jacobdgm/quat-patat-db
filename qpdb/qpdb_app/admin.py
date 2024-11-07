from django.contrib import admin
from .models import (
    Tune,
    Set,
    Performance,
)

admin.site.register(Tune)
admin.site.register(Set)
admin.site.register(Performance)

