from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tunes/<int:pk>', views.TuneDetailView.as_view(), name='tune-detail-view'),
    path('medleys/<int:pk>', views.MedleyDetailView.as_view(), name='medley-detail-view'),
]
