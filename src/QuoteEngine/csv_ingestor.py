from ingestor_interface import IngestorInterface
from quote_model import QuoteModel
import csv


class CSVIngestor(IngestorInterface):
    """A class to ingest quotes from CSV files."""
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path):
        """Parse a CSV file containing quotes.

        Args:
            path (str): The path to the CSV file.

        Returns:
            list: A list of QuoteModel objects representing the quotes.
        """
        quote_list = []
        if cls.can_ingest(path):
            with open(path, 'r') as f:
                reader = csv.DictReader(f)
                for elem in reader:
                    body = elem['body']
                    author = elem['author']
                    quote = QuoteModel(body, author)
                    quote_list.append(quote)
            return quote_list
        else:
            return quote_list
