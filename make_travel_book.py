
from ZipHandler import ZipHandler

zip_dir = "./blog_zips"
book_dir = "./travel_book"

zh = ZipHandler(zip_dir)
zh.unzip(book_dir)

