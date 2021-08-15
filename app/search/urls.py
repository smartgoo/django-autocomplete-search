from django.urls import path

from .views import autocomplete

app_name = 'search'

urlpatterns = [
    path('autocomplete/', autocomplete, name='autocomplete')
]