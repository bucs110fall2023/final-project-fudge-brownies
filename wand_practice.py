from wand.image import Image

with Image(filename="IMG_E2594.jpg") as img:
    img.transform_colorspace('gray')
    img.edge(radius=1)
    img.save(filename="effect-edge.jpg")