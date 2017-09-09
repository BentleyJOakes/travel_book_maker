import os
from html.parser import HTMLParser
from templates import write_header, write_footer

class LatexHandler:

    def __init__(self, book_dir):
        self.book_dir = book_dir

        self.book_title = None
        self.book_author = None

        self.out_file = None

        self.temp_data = None
        self.in_title = False

        self.skip_tags = ["p", "h1", "a"]
        self.title_tags = ["h2", "strong"]

    def make_book(self, title, author):
        self.book_title = title
        self.book_author = author

        files = os.listdir(self.book_dir)
        files = [f for f in files if f.endswith(".html")]

        main_filename = os.path.join(self.book_dir, "main.tex")
        with open(main_filename, 'w') as f:
            write_header(f, self.book_title, self.book_author)

            for fil in sorted(files):

                blog_name = fil.split("-")[0]
                blog_file = self.make_blog_file(blog_name, fil)
                f.write(r"\input{" + blog_file + "}\n")

        with open(main_filename, 'a') as f:
            write_footer(f)



    def make_blog_file(self, blog_name, html_filename):
        filename = os.path.join(self.book_dir, html_filename)

        tex_filename = os.path.join(self.book_dir, blog_name + ".tex")

        with open(filename) as f:

            with open(tex_filename, 'w') as g:

                self.out_file = g

                parser = Parser(self.handle_starttag, self.handle_endtag, self.handle_data)

                parser.feed(f.readline())

        return blog_name



    def write_text(self, text):
        self.out_file.write(text)

    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            return

        if tag in self.title_tags:
            self.in_title = True

        print("Encountered a start tag:", tag, str(attrs))

        #if tag == "h1":


    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            return

        print("Encountered an end tag :", tag)

        if tag in self.title_tags:

            print("Out: " + self.temp_data)
            self.in_title = False


    def handle_data(self, data):
        print("Encountered some data  :", data)
        self.temp_data = data

        if not self.in_title:

            #print("Out: " + self.temp_data)
            self.write_text(self.temp_data + "\n")



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