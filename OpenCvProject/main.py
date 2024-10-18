import cv2
import numpy as np

img = cv2.imread("img/436769167_1196846951690341_5217558474686322680_n.jpg")

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print(img_gray.shape)

img_resize=cv2.resize(img,(256,256))
cv2.imshow("window",img_resize)
cv2.waitKey(0)