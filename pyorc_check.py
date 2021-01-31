from PIL import Image
import pyocr
import pyocr.builders

fname = '数字.png'
im = Image.open(fname)

tool = pyocr.get_available_tools()[0]
text = tool.image_to_string(im, lang='eng', builder=pyocr.builders.TextBuilder())
text.rstrip("\n")

# text.replace("\n", "")
print(text)
