import cv2
import numpy as np 

img = cv2.imread(r"D:\pyrhon_test\4.Hough Transform Detection\circle.png", 0)
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=100, maxRadius=200)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    #換外圓
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    #畫出圓心
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
cv2.imshow('detect circles', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()