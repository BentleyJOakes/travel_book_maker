from zipfile import ZipFile
import os
import sys
import shutil

class ZipHandler:

    def __init__(self, zip_dir):
        self.zip_dir = zip_dir

    def unzip(self, target_dir):
        files = os.listdir(self.zip_dir)

        files = [os.path.join(self.zip_dir, f) for f in files if f.endswith(".zip")]
        files.sort(key = lambda x: os.path.getctime(x))
        files.reverse()
        for i, zip_filename in enumerate(files):
            print(zip_filename)

            html_file = None
            with ZipFile(zip_filename) as myzip:


                for f in myzip.infolist():

                    if f.filename.endswith("html"):
                        html_file = f.filename

                myzip.extractall(target_dir)

            if html_file is None:
                raise Exception("Couldn't find html file!")

            html_filename = os.path.join(target_dir, html_file)
            new_html_filename = os.path.join(target_dir, "blog"+str(i) + "-" + html_file)

            os.rename(html_filename, new_html_filename)

            images_dir = os.path.join(target_dir, "images/")
            new_images_dir = os.path.join(target_dir, "blog"+str(i) + "-" + "images/")
            shutil.move(images_dir, new_images_dir)

