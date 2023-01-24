import cv2
import imutils
import time
import tkinter as tk
from tkinter import filedialog


def detect_people(input_file):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    if (input_file.endswith('jpg')):
        # Reading the Image
        image = cv2.imread(input_file)

        # Resizing the Image
        image = imutils.resize(image,
                               width=min(400, image.shape[1]))

        # Detecting all the regions in the
        # Image that has a pedestrians inside it
        (regions, _) = hog.detectMultiScale(image,
                                            winStride=(4, 4),
                                            padding=(4, 4),
                                            scale=1.05)

        # Drawing the regions in the Image
        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y),
                          (x + w, y + h),
                          (0, 0, 255), 2)

        # Showing the output Image
        cv2.imshow("Image", image)
        cv2.waitKey(0)

        cv2.destroyAllWindows()
    else:
        cap = cv2.VideoCapture(input_file)
        while cap.isOpened():
            ret, image = cap.read()
            if ret:
                image = imutils.resize(image,
                                       width=min(400, image.shape[1]))

                (regions, _) = hog.detectMultiScale(image,
                                                    winStride=(4, 4),
                                                    padding=(4, 4),
                                                    scale=1.05)

                # Drawing the regions in the
                # Image
                for (x, y, w, h) in regions:
                    cv2.rectangle(image, (x, y),
                                  (x + w, y + h),
                                  (0, 0, 255), 2)

                # Showing the output Image
                cv2.imshow("Image", image)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()


def open_file_explorer():
    root = tk.Tk()
    root.withdraw()
    input_file = filedialog.askopenfilename()
    detect_people(input_file)


open_file_explorer()
