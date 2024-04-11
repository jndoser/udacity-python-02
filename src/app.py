import random
import os
import requests
from flask import Flask, render_template, abort, request


# @TODO Import your Ingestor and MemeEngine classes
from src.MemeEngine.meme_generator import MemeEngine
from src.QuoteEngine import Ingestor
import tempfile
import datetime

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for quote_file in quote_files:
        quotes.extend(Ingestor.parse(quote_file))

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = None
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array
    img = random.choice(imgs)

    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.
    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    if image_url != '':
        response = requests.get(image_url)

        img = f'{tempfile.gettempdir()}-' + datetime.date.today().strftime("%B %d, %Y") + '.jpeg'
        with open(img, 'wb') as out:
            out.write(response.content)
    else:
        img = random.choice(imgs)

    if not body:
        body = random.choice(quotes).body

    if not author:
        author = random.choice(quotes).author

    path = meme.make_meme(img, body, author)

    if image_url != '':
        os.remove(img)

    return render_template('meme.html', path)


if __name__ == "__main__":
    app.run()
