import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread("bild.jpg")
print(img.shape)

i = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(i)
plt.show()

g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)




