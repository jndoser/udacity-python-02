from ingestor_interface import IngestorInterface
from text_ingestor import TextIngestor
from csv_ingestor import CSVIngestor
from doc_ingestor import DocIngestor
from pdf_ingestor import PDFIngestor


class Ingestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        for ingestor in [TextIngestor, CSVIngestor, DocIngestor, PDFIngestor]:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
