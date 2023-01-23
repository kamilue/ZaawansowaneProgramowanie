import cv2
import time
import tkinter as tk
from tkinter import filedialog


def detect_people(input_file):
    # Wczytanie pliku
    cap = cv2.VideoCapture(input_file)
    if not cap.isOpened():
        print("Nie można otworzyć pliku")
        return

    # Ustawienie klasyfikatora
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Pętla przez klatki w filmie lub pojedyncze zdjęcie
    start_time = time.time()
    people_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))  # zmniejszenie rozdzielczości klatek
        boxes, _ = hog.detectMultiScale(frame, winStride=(8, 8), padding=(32, 32), scale=1.1)
        # zwiększenie skali detekcji
        for (x, y, w, h) in boxes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            people_count += 1

        cv2.imshow("People detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    end_time = time.time()
    cap.release()
    print("Czas detekcji: {:.2f}s".format(end_time - start_time))
    print("Liczba wykrytych osób: {}".format(people_count))
    root = tk.Tk()
    root.withdraw()
    root.destroy()


def open_file_explorer():
    root = tk.Tk()
    root.withdraw()
    input_file = filedialog.askopenfilename()
    detect_people(input_file)


open_file_explorer()
