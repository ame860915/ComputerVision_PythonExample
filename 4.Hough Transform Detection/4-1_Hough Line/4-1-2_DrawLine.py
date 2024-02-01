import numpy as np 
import cv2
import matplotlib.pyplot as plt 

img = cv2.imread(r"D:\pyrhon_test\4.Hough Transform Detection\Road.bmp")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #灰階影像
edges = cv2.Canny(gray, 50, 200)
plt.subplot(121)
plt.imshow(edges, 'gray')
plt.xticks([]), plt.yticks([])

#hough變換
lines = cv2.HoughLines(edges, 1, np.pi / 180, 160)
lines1 = lines[:, 0, :] #提取二維
for rho, theta in lines1[:]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 + 1000 * (-b))
    y2 = int(y0 + 1000 * (a))
    cv2.line(img, (x1, y1),(x2, y2), (255, 0, 0), 1)

plt.subplot(122)
plt.imshow(img,)
plt.xticks([]), plt.yticks([])
plt.show