import os

def cleanup():
    if os.path.isdir("temp"):
        for root, dirs, files in os.walk("temp", topdown=False):
            for name in files:
                os.remove(os.path.join(root,name))
            for name in dirs:
                os.rmdir(os.path.join(root,name))
        print("Ready to go!")
    else:
        os.mkdir("temp")
