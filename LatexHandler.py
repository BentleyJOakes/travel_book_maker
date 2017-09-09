import os
from html.parser import HTMLParser


class LatexHandler:

    def __init__(self, book_dir):
        self.book_dir = book_dir

    def make_book(self, title):
        print(title)
        print(self.book_dir)

        files = os.listdir(self.book_dir)
        files = [f for f in files if f.endswith(".html")]

        for f in sorted(files):

            blog_name = f.split("-")[0]
            self.make_blog_file(blog_name, f)


    def make_blog_file(self, blog_name, html_filename):
        filename = os.path.join(self.book_dir, html_filename)

        tex_filename = os.path.join(self.book_dir, blog_name + ".tex")

        with open(filename) as f:

            with open(tex_filename, 'w') as g:

                parser = Parser(self.handle_starttag, self.handle_endtag, self.handle_data)

                parser.feed(f.readline())

                #g.write(blog_name)

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)



class Parser(HTMLParser):

    def __init__(self, handle_starttag, handle_endtag, handle_data):
        super(Parser, self).__init__()
        self.over_handle_starttag = handle_starttag
        self.over_handle_endtag = handle_endtag
        self.over_handle_data = handle_data

    def handle_starttag(self, tag, attrs):
        self.over_handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        self.over_handle_endtag(tag)

    def handle_data(self, data):
        self.over_handle_data(data)