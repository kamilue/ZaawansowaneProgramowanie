import cv2


def read_image(path: str):
    return cv2.imread(path)
