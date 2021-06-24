import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread("bild.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#plt.imshow(gray, "gray")
#plt.show()


classifier = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
face = classifier.detectMultiScale(gray, minNeighbors=10)

print(face)


c = img.copy()
for f in face:
    x, y, w, h = f
    cv2.rectangle(c, (x, y), (x + w, y + h), (0, 255, 0), 10)
    print(f)

i = cv2.cvtColor(c, cv2.COLOR_BGR2RGB)
plt.imshow(i)
plt.show()

