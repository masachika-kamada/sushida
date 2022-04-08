import cv2
import pyocr
import pyocr.builders

pyocr.tesseract.TESSERACT_CMD = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
tool = pyocr.get_available_tools()[0]


def ocr(img_path, pre_text, ng_idx, ymin, ymax, xmin, xmax):
    img = cv2.imread(img_path, 0)[ymin:ymax, xmin:xmax]
    img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

    # tool で文字を認識させる
    text = tool.image_to_string(
        img, lang='eng', builder=pyocr.builders.TextBuilder())

    print(text)

    if not text.islower() or ")" in text or text == pre_text:
        cv2.imwrite(f"./mistakes/pic_{ng_idx}.jpg", img)
        return False, None

    return text.replace(" ", "")
