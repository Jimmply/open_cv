import cv2
import numpy as np

img = cv2.imread("data/scihub.jpg")
print(img.shape)

imgResize = cv2.resize(img,(480, 320))
print(imgResize.shape)

imgCropped = img[0:320,200:520]

cv2.imshow("Image", img)
cv2.imshow("Resized image", imgResize)
cv2.imshow("Cropped image", imgCropped)
cv2.waitKey(0)