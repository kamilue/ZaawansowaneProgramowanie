from flask import Flask, request
import cv2
import numpy as np
import requests
import time

app = Flask(__name__)


@app.route('/detect_people', methods=['GET'])
def detect_people_api():
    url = request.args.get('url')
    people_count, detection_time = detect_people(url)
    return f"Detekcja zakończona. Czas detekcji: {detection_time:.2f}s. Liczba wykrytych osób: {people_count}"


def detect_people(url):
    # Pobieranie pliku
    response = requests.get(url)
    img_array = np.array(bytearray(response.content), dtype=np.uint8)
    frame = cv2.imdecode(img_array, -1)

    # Ustawienie klasyfikatora
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Pętla przez klatki w filmie lub pojedyncze zdjęcie
    start_time = time.time()
    people_count = 0

    frame = cv2.resize(frame, (640, 480))  # zmniejszenie rozdzielczości klatek
    boxes, _ = hog.detectMultiScale(frame, winStride=(8, 8), padding=(32, 32), scale=1.1)
    # zwiększenie skali detekcji
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        people_count += 1
        cv2.imshow("People detection", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    end_time = time.time()
    detection_time = end_time - start_time
    return people_count, detection_time


if __name__ == '__main__':
    app.run(debug=True)
