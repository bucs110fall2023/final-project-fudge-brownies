import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageFilter


source = askopenfilename()
#print(source)
im = Image.open(source)

gray_im = im.convert("L")
#blur_im = gray_im.filter(ImageFilter.BLUR)
smooth_im = im.filter(ImageFilter.SMOOTH)
filter_im = smooth_im.filter(ImageFilter.FIND_EDGES)
filter_im.show()