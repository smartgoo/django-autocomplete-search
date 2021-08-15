import re

from django.core.cache import cache


class SearchResults():
    """
    A class that holds the search results
    """

    def __init__(self, results: list, count: int) -> None:
        """
        :param query: the search query entered by the user on the site
        :param index: the search index to search over
        """
        self.results = results
        self.count = count


class SearchIndex():
    """
    A class for creating search indexes
    """

    def __init__(self, data: list) -> None:
        """
        :param data: the data we want to create the index for
        """
        self.data = data
        self.index_length = len(data)
        self.index = self._generate_index()

    def _generate_index(self) -> list:
        """
        Generates search index during initialization
        """
        index = [{"ticker": each[0],"name": each[1]} for each in self.data]
        index = sorted(index, key = lambda i: i['ticker'])
        return index

    def search(self, query: str) -> SearchResults:
        """
        Called from the view to search the index. 
        :param query: the search query entered by the user
        """
        results = []

        for doc in self.index:
            # search on ticker
            if re.match(query, doc['ticker'],re.I):
                results.append({'ticker': doc['ticker'], 'name': doc['name']})
            
            # search on name
            if (
                re.match(query, doc['name'],re.I)
                and {'ticker': doc['ticker'], 'name': doc['name']} not in results
            ):
                results.append({'ticker': doc['ticker'], 'name': doc['name']})
        
        count = len(results)
        return SearchResults(results, count)
