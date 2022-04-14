import cv2
import numpy as np

img = np.zeros((512, 512, 3))
#print(img.shape)
#img[100:300,200:300]=255,0,0

cv2.line(img,(0,0),(300,300),(0,255,255),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.circle(img,(400, 50),30,(255,255,0),0)
cv2.putText(img,"Open CV", (200,100),cv2.FONT_HERSHEY_PLAIN,2,(150,250,0),1)

cv2.imshow("Image", img)

cv2.waitKey(0)