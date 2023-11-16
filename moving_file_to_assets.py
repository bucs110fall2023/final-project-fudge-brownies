import tkinter as tk
from tkinter.filedialog import askopenfilename
import shutil
import os

tk.Tk().withdraw() # part of the import if you are not using other tkinter functions

source = askopenfilename()
#the code above opens the file explorer to select a file

shutil.copy(source, ) #need help moving file to assets folder + making it work for all show links at bookmarks

print("File copied successfully.")
 
