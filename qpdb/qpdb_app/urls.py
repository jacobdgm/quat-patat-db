from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tunes/<int:pk>', views.TuneDetailView.as_view()),
]
