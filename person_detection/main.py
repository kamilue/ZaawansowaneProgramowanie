import cv2
import imutils
import time
import tkinter as tk
from tkinter import filedialog


def detect_people(input_file):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    if (input_file.endswith('jpg')):
        image = cv2.imread(input_file)

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


def open_file_explorer():
    root = tk.Tk()
    root.withdraw()
    input_file = filedialog.askopenfilename()
    detect_people(input_file)


open_file_explorer()
