class ImageHandler:

    def __init__(self):
        self.outfile = None
        self.images = []


    def add_image(self, image):
        self.images.append(image)

    def flush(self):

        if not self.images:
            return

        self.write_header()

        for img in self.images:
            self.write_image(img, len(self.images))

        self.write_footer()

        self.images = []


    def write_header(self):
        self.outfile.write(r"""
        \begin{figure*}[h!]
            \centering""")

    def write_footer(self):
        self.outfile.write(r"""%\caption*{}
    \end{figure*}
""")

    def write_image(self, image_file, num_images):

        size = "0.80"
        if num_images > 1:
            size = "0.49"

        self.outfile.write(r"""\begin{subfigure}[t]{""")
        self.outfile.write(size)
        self.outfile.write(r"""\textwidth}
            \includegraphics[width=\linewidth]{""")
        self.outfile.write(image_file)
        self.outfile.write(r"""}
        \end{subfigure}
""")