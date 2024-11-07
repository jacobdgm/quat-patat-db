from django.shortcuts import render
from django.http import HttpResponse

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
