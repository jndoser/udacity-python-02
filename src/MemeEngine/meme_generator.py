from PIL import Image, ImageDraw, UnidentifiedImageError
import random
import os
import datetime


class MemeEngine:
    """A class for generating memes."""

    def __init__(self, output_dir):
        """Initialize the MemeEngine.

        Args:
            output_dir (str): The directory where generated memes will be saved.
        """
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500):
        """Generate a meme.

        Args:
            img_path (str): The path to the image file.
            text (str): The text to be added to the meme.
            author (str): The author of the quote.
            width (int, optional): The width of the meme image. Defaults to 500.

        Returns:
            str: The path to the generated meme image.
        """
        try:
            img = Image.open(img_path)
        except (FileNotFoundError, UnidentifiedImageError):
            raise ValueError("Invalid image file")

        resized_img = img.resize((
            int(width),
            int(width / img.width * img.height)
        ))

        quote = f'"{text}" - {author}'

        draw_img = ImageDraw.Draw(resized_img)
        text_position = (
            random.randint(0, max(0, resized_img.width - 300)),
            random.randint(0, max(0, resized_img.height - 100))
        )
        draw_img.text(text_position, quote)

        output_img_path = os.path.join(
            self.output_dir,
            datetime.date.today().strftime("%B %d, %Y") + '.png'
        )

        os.makedirs(self.output_dir, exist_ok=True)
        resized_img.save(output_img_path)

        return output_img_path
