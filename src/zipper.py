import zipfile
from shutil import copy2,rmtree,make_archive

from subprocess import call
import os

class Zipper:
    def __init__(self,path,file_name):
        self.path=path
        self.file_name = file_name

        if not os.path.isdir("temp"):
            os.mkdir("temp")
        copy2(path + file_name,"temp/")

        self.zip_file = self.file_name[:-4] + "zip"
        os.rename("temp/" + self.file_name,"temp/" + self.zip_file)


    def unpack(self):
        zip_ref = zipfile.ZipFile("temp/" + self.zip_file, 'r')
        zip_ref.extractall("temp/")
        zip_ref.close()

    def pack(self):
        make_archive(self.zip_file,'zip', 'temp')
