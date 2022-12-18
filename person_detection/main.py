import cv2

image = cv2.imread('people1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

bboxes = classifier.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in bboxes:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

count = len(bboxes)
print(f'{count} people detected')

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
