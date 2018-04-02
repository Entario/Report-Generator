import config as cf
from zipper import Zipper
import cleaner

cleaner.cleanup()

zip = Zipper("Templates/","Test_Template.docx")
zip.unpack()

zip.pack()
