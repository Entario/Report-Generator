import config as cf
from zipper import Zipper
import cleaner

cleaner.cleanup()

zip = Zipper("Templates/","Test_Template.docx")
zip.unpack()

config = cf.Config("Configs/test_config")
dict = config.get_dict()

with open("temp/word/document.xml", 'r') as f:
    lines = f.readlines()
    # for line in lines:
    #     wordlist = line.split(' ')
    #     # print(wordlist)
    #     for word in wordlist:
    #         if '$$' in word:
    #             start = "<w:t>"
    #             end = "</w:t>"
    #             varlist.append(word[word.find(start)+len(start):word.rfind(end)].upper())

with open("temp/word/document.xml", 'w') as f:
    for line in lines:
        if '$$' in line:
            for key in dict.keys():
                line = line.replace('$$' + key, dict[key])
                print('$$' + key, dict[key])
            f.write(line)
        else:
            f.write(line)

print(dict)
zip.pack()
