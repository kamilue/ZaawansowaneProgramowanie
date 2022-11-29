from functions.read_text_from_image import read_text_from_image


def get_texts_from_images(pictures):
    [
        print(f"{picture}\n\n" + read_text_from_image(picture))
        for picture in pictures
    ]
