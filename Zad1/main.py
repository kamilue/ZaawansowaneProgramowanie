import pytesseract
from functions.get_texts_from_images import get_texts_from_images

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\\Users\\Kamil Plekaniec\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
)

get_texts_from_images(
    [
        r"pictures\\picture1.png",
        r"pictures\\picture2.png",
        r"pictures\\picture3.jpg",
        r"pictures\\picture4.jpg",
        r"pictures\\picture5.png",
    ]
)
