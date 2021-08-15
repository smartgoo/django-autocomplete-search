import re

from django.core.cache import cache
from django.shortcuts import render


# Create your views here.
def autocomplete(request):
    query = request.GET.get('search').lower()

    index = cache.get('tickers_search_index')
    results = index.search(query)
   
    ctx = {
        'results': results.results,
        'results_count': results.count
    }

    return render(request, 'search_results.html', context=ctx)