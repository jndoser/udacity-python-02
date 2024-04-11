from ingestor_interface import IngestorInterface
from quote_model import QuoteModel
from docx import Document


class DocIngestor(IngestorInterface):
    """A class to ingest quotes from DOCX files."""
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path):
        """Parse a DOCX file containing quotes.

        Args:
            file_path (str): The path to the DOCX file.

        Returns:
            list: A list of QuoteModel objects representing the quotes.
        """
        quote_list = []
        if cls.can_ingest(path):
            doc = Document(path)
            for para in doc.paragraphs:
                text = para.text.strip()
                if len(text) > 0:
                    contents = text.split('-')
                    body, author = contents[0].strip('"').strip(), contents[1].strip()
                    quote = QuoteModel(body, author)
                    quote_list.append(quote)
            return quote_list
        else:
            return quote_list
