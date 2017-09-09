
from DOCXHandler import DOCXHandler

book_dir = "./travel_book"
docx_dir = "./blog_docx"

dh = DOCXHandler(docx_dir)

dh.extract(book_dir)



