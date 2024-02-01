import cv2
import numpy as np

def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
    detected_edges = cv2.Canny(detected_edges,
                                lowThreshold,
                                lowThreshold * ratio,
                                apertureSize = kernel_size)
    dst = cv2.bitwise_and(img2, img2, mask = detected_edges)  #只需要在原始影像邊緣增加一些顏色
    cv2.imshow('canny demo', dst)

lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3
img1 = cv2.imread(r"D:\pyrhon_test\1.Common Libraries\Lenna.bmp", 0)
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)    #cv通道為BGR，但plt.show讀取為RGB
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)    #cv通道為BGR，但plt.show讀取為RGB

cv2.namedWindow('canny demo')
cv2.createTrackbar('Min threshold', 'canny demo', lowThreshold, max_lowThreshold, CannyThreshold)

CannyThreshold(0)   #初始化
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()