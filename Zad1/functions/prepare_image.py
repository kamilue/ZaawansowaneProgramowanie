import cv2
from functions.read_image import read_image


def prepare_image(path: str):
    img = cv2.cvtColor(read_image(path), cv2.COLOR_BGR2GRAY)
    return cv2.adaptiveThreshold(
        cv2.bilateralFilter(img, 9, 75, 75),
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        2,
    )
