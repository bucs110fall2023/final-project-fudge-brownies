import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image


source = askopenfilename()
print(source)
im = Image.open(source)
im.show()

