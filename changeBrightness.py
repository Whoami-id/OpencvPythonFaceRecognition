import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread("bild.jpg")

z = np.zeros((1000, 1500, 3), dtype="uint8") + 50

increased = cv2.add(img, z)

i = cv2.cvtColor(increased, cv2.COLOR_BGR2RGB)
plt.imshow(i)
plt.show()


