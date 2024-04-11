from ingestor_interface import IngestorInterface
from quote_model import QuoteModel
import tempfile
import subprocess
import datetime
import os


class PDFIngestor(IngestorInterface):
    """A class for ingesting quotes from PDF files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path):
        """Parse a PDF file containing quotes.

        Args:
            path (str): The path to the PDF file.

        Returns:
            list: A list of QuoteModel objects representing the quotes.
        """
        quote_list = []
        if not cls.can_ingest(path):
            return quote_list

        temp_file_path = os.path.join(tempfile.gettempdir(), f'{datetime.date.today().strftime("%B %d, %Y")}.txt')
        subprocess.run(['pdftotext', path, temp_file_path])

        with open(temp_file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    body, author = map(str.strip, line.split('-', 1))
                    quote = QuoteModel(body.strip('"'), author.strip())
                    quote_list.append(quote)

        os.remove(temp_file_path)
        return quote_list
