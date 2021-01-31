from skimage import io
from PIL import Image

# I = io.imread('mistakes/pic.png')
# io.show(I)

fname = 'mistakes/pic.png'
im = Image.open(fname)

im = im.convert("L")
for i in range(im.size[0]):
    for j in range(im.size[1]):
        if im.getpixel((i, j)) >= 128:
            im.putpixel((i, j), 0)
        else:
            im.putpixel((i, j), 255)

im.save('gray.png')
