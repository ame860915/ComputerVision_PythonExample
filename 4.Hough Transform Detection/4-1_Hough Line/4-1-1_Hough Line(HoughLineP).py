import numpy as np 
import cv2

lane = cv2.imread(r"D:\pyrhon_test\4.Hough Transform Detection\Road.bmp")
#高斯模糊，Canny邊緣檢測需要的
lane = cv2.GaussianBlur(lane, (5, 5), 0)
#進行邊緣檢測，減少影像空間中需要檢測的數量
lane = cv2.Canny(lane, 50, 150)
cv2.imshow('lane', lane)
cv2.waitKey()

rho = 1 #距離解析度
theta = np.pi / 180     #角度解析度
threshold = 10          #霍夫空間中多少個曲線相交才算作正式焦點
min_line_len = 10       #最少多少個像素點才組成一條直線
max_line_gap = 50       #線段之間的最大間隔像素

lines = cv2.HoughLinesP(lane, rho, theta, threshold, maxLineGap=max_line_gap)
line_img = np.zeros_like(lane)
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(line_img, (x1, y1), (x2, y2), 255, 1)
cv2.imshow('line_img', line_img)
cv2.waitKey()
