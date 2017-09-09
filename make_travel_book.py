
from DOCXHandler import DOCXHandler
from LatexHandler import LatexHandler

import configparser

config = configparser.ConfigParser()
config.read('config.cfg')

book_title = config.get('TravelBook', 'title')
book_author = config.get('TravelBook', 'author')

docx_dir = config.get('TravelBook', 'input_dir')
book_dir = config.get('TravelBook', 'output_dir')

dh = DOCXHandler(docx_dir)

dh.extract(book_dir)

lh = LatexHandler(book_dir)
lh.make_book(book_title, book_author)

