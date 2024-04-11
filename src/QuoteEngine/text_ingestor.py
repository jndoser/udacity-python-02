from ingestor_interface import IngestorInterface
from quote_model import QuoteModel


class TextIngestor(IngestorInterface):
    """A class for ingesting quotes from text files (.txt)."""
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path):
        """Parse a text file containing quotes.

        Args:
            path (str): The path to the text file.

        Returns:
            list: A list of QuoteModel objects representing the quotes.
        """
        quote_list = []
        if not cls.can_ingest(path):
            return quote_list

        with open(path, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    body, author = map(str.strip, line.split('-', 1))
                    quote = QuoteModel(body.strip('"'), author.strip())
                    quote_list.append(quote)

        return quote_list
