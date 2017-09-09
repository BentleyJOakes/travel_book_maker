
from DOCXHandler import DOCXHandler
from LatexHandler import LatexHandler

book_dir = "./travel_book"
docx_dir = "./blog_docx"

dh = DOCXHandler(docx_dir)

dh.extract(book_dir)

lh = LatexHandler(book_dir)
lh.make_book("Travel Blog")

