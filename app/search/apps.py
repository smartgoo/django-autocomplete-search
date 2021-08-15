import csv
from pathlib import Path

from django.apps import AppConfig
from django.core.cache import cache

from app.settings import BASE_DIR
from .utils import SearchIndex

class SearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'search'

    def ready(self):
        """
        Creates the search index when the Django project boots.
        1. Reads from tickers.csv (just for demo purposes)
        2. Creates two search indexes
        3. Stores index in Django cache

        Read from your database, an API, or alternate information source here.
        """

        # Read from tickers.csv
        tickers_csv = Path(BASE_DIR / 'tickers.csv')
        with open(tickers_csv) as file:
            r = csv.reader(file)
            data = [row for row in r][1:]

        # Create search indexes
        index = SearchIndex(data)

        # Store search index in cache
        cache.set('tickers_search_index', index, None)
        return
