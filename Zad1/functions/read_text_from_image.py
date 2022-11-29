import pytesseract
from functions.prepare_image import prepare_image


def read_text_from_image(path: str) -> str:
    return pytesseract.image_to_string(
        prepare_image(path),
    )
