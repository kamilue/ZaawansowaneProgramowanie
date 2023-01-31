from flask import Flask, request
import cv2
<<<<<<< HEAD
import imutils
=======
import numpy as np
import requests
>>>>>>> person_detection
import time

app = Flask(__name__)


<<<<<<< HEAD
def detect_people(input_file):
=======
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
>>>>>>> person_detection
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    if (input_file.endswith('jpg')):
        image = cv2.imread(input_file)

<<<<<<< HEAD
        image = imutils.resize(image,
                               width=min(400, image.shape[1]))

        (regions, _) = hog.detectMultiScale(image,
                                            winStride=(4, 4),
                                            padding=(4, 4),
                                            scale=1.05)

        start_time = time.time()
        people_count = 0
        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y),
                          (x + w, y + h),
                          (0, 0, 255), 2)
            people_count += 1

        cv2.imshow("People detection", image)
        end_time = time.time()
        cv2.waitKey(0)
        print("Czas detekcji: {:.2f}s".format(end_time - start_time))
        print("Liczba wykrytych osób: {}".format(people_count))
        cv2.destroyAllWindows()
    else:
        cap = cv2.VideoCapture(input_file)
        start_time = time.time()
        people_count = 0
        while cap.isOpened():
            ret, image = cap.read()
            if ret:
                image = imutils.resize(image,
                                       width=min(400, image.shape[1]))

                (regions, _) = hog.detectMultiScale(image,
                                                    winStride=(4, 4),
                                                    padding=(4, 4),
                                                    scale=1.05)

                for (x, y, w, h) in regions:
                    cv2.rectangle(image, (x, y),
                                  (x + w, y + h),
                                  (0, 0, 255), 2)
                    people_count += 1

                cv2.imshow("People detection", image)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break

        end_time = time.time()
        cap.release()
        cv2.destroyAllWindows()

        print("Czas detekcji: {:.2f}s".format(end_time - start_time))
        print("Liczba wykrytych osób: {}".format(people_count))
=======
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
>>>>>>> person_detection


if __name__ == '__main__':
    app.run(debug=True)
