import re

class SearchResults():
    """
    A class that holds the search results
    """

    def __init__(self, results: list, count: int) -> None:
        """
        :param query: the search query entered by the user on the site
        :param index: the search index to search over
        """
        self.results: list = results
        self.count: int = count

 
class SearchIndex():
    """
    A class for creating search indexes
    """

    def __init__(self, data: list) -> None:
        """
        :param data: the data we want to create the index for
        """
        self.raw_data: list = data
        self.index_length: int = len(data)
        self.index: list = self._generate_index()

    def _generate_index(self) -> list:
        """
        Generates search index during initialization
        """

        # Iterate over raw data from csv and create an index
        index = [{"ticker": each[0],"name": each[1]} for each in self.raw_data]

        # Sort the index by alphabetically by ticker
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
            if re.match(query, doc['ticker'], re.I):
                results.append({'ticker': doc['ticker'], 'name': doc['name']})
            
            # search on name
            if (
                re.match(query, doc['name'], re.I)
                and {'ticker': doc['ticker'], 'name': doc['name']} not in results
            ):
                results.append({'ticker': doc['ticker'], 'name': doc['name']})
        
        count = len(results)
        return SearchResults(results, count)
