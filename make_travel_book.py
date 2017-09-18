
from DOCXHandler import DOCXHandler
from LatexHandler import LatexHandler

import os
import configparser

import argparse

config = configparser.ConfigParser()
config.read('config.cfg')

book_title = config.get('TravelBook', 'title')
book_author = config.get('TravelBook', 'author')

docx_dir = config.get('TravelBook', 'input_dir')
book_dir = config.get('TravelBook', 'output_dir')


parser = argparse.ArgumentParser(description='Run the script to make the travel book.')
parser.add_argument('--force', dest = 'force_run', action = 'store_true',
                        help = 'Force the script to run if the output directory is non-empty.')
parser.set_defaults(force_run = False)

args = parser.parse_args()
if not args.force_run and os.path.exists(book_dir):
    raise Exception("Error: Directory already exists! Use --force to overwrite directory.")

if not os.path.exists(book_dir):
    os.mkdir(book_dir)

dh = DOCXHandler(docx_dir)

dh.extract(book_dir)

lh = LatexHandler(book_dir)
lh.make_book(book_title, book_author)

