from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from qpdb_app.models import Tune

index_html = """
    <title>
        The Quatre Patates Database
    </title>
    <body>
    <h1>
        The Quatre Patates Database
    </h1>
    <p>Welcome to the Quatre Patates Database!
"""

def index(request):
    return HttpResponse(index_html)

class TuneDetailView(DetailView):
    model = Tune
    template_name = "qpdb_app/tune_detail.html"
