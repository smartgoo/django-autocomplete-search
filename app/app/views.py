from django.shortcuts import render

from .settings import TEMPLATE_DIR, BASE_DIR

def home(request):
    return render(request, 'base.html')