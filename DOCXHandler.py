
import mammoth

import os
import sys
import shutil

class DOCXHandler:

    def __init__(self, docx_dir):
        self.docx_dir = docx_dir

        self.image_counter = 0
        self.image_dir = None

        self.target_dir = None


    def extract(self, target_dir):

        self.target_dir = target_dir

        files = os.listdir(self.docx_dir)

        files = [os.path.join(self.docx_dir, f) for f in files if f.endswith(".docx")]
        files.sort(key = lambda x: os.path.getctime(x))
        files.reverse()
        for i, docx_filename in enumerate(files):
            print(docx_filename)

            self.image_dir = "blog" + str(i) + "_images"
            if not os.path.exists(os.path.join(target_dir, self.image_dir)):
                os.mkdir(os.path.join(target_dir, self.image_dir))

            html_name = "blog" + str(i) + "-" + str(docx_filename.split("/")[-1]).replace(".docx", ".html")
            with open(target_dir + "/" + html_name, 'w') as html_file:
                with open(docx_filename, "rb") as docx_file:
                    result = mammoth.convert_to_html(docx_file, convert_image=mammoth.images.img_element(self.convert_image))
                    html = result.value  # The generated HTML
                    messages = result.messages  # Any messages, such as warnings during conversion
                    if messages:
                        raise Exception(messages)

                    html_file.write(html)

    def convert_image(self, image):
        with image.open() as image_bytes:

            image_filename = "image" + str(self.image_counter) + "." + str(image.content_type.split("/")[-1])
            self.image_counter += 1

            full_image_filename = os.path.join(self.target_dir, self.image_dir, image_filename)

            with open(full_image_filename, 'wb') as img:
                img.write(image_bytes.read())
        #    encoded_src = base64.b64encode(image_bytes.read()).decode("ascii")

        #image.
        #image.

        return {
            #"src": "data:{0};base64,{1}".format(image.content_type, encoded_src)
            "src" : os.path.join(self.image_dir, image_filename)

        }