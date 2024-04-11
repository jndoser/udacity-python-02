class QuoteModel:
    """
        Represents a quote model consisting of a body and an author.

        Attributes:
            body (str): The body of the quote.
            author (str): The author of the quote.
    """
    def __init__(self, body, author):
        """
            Initializes a QuoteModel object with the given body and author.

            Args:
                body (str): The body of the quote.
                author (str): The author of the quote.
        """
        self.body = body
        self.author = author

    def __str__(self):
        """
            Returns a string representation of the quote in the format:
            "<quote_body>" - <quote_author>

            Returns:
                str: A string representation of the quote.
        """
        return f'"{self.body}" - {self.author}'

    def __repr__(self):
        """
            Returns a string representation of the QuoteModel object.

            Returns:
                str: A string representation of the QuoteModel object.
        """
        return f"QuoteModel(body={self.body}, author={self.author})"