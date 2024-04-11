import abc
from abc import ABC


class IngestorInterface(ABC):
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """
            Check if the class can ingest a file based on its extension.

            Args:
                path (str): The path of the file.

            Returns:
                bool: True if the file can be ingested, False otherwise.
        """
        extension = path.split(".")[1]
        return cls.allowed_extensions.count(extension) > 0

    @classmethod
    @abc.abstractmethod
    def parse(cls, path):
        """
        Parse a file.

        This method should be implemented by subclasses to parse
        a file with a specific format.

        Args:
            path (str): The path of the file.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError
    