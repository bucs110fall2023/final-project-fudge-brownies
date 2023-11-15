import tkinter as tk
from tkinter.filedialog import askopenfilename
import shutil
import os

tk.Tk().withdraw() # part of the import if you are not using other tkinter functions

asset_to_draw = askopenfilename()
#the code above opens the file explorer to select a file
 
source = '/home/tuhingfg/Documents/source'
destination = '/home/tuhingfg/Documents/destination'
 
# gather all files
allfiles = os.listdir(source)
 
# iterate on all files to move them to destination folder
for f in allfiles:
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, f)
    shutil.move(src_path, dst_path)

#the code above is to move file from one place to another (still needs to be worked on)