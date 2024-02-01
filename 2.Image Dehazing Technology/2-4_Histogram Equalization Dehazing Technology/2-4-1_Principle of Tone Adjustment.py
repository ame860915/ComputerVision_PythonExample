import cv2
import numpy as np

img = cv2.imread(r"D:\pyrhon_test\2.Image Dehazing Technology\Lenna.bmp", 0)
equ = cv2.equalizeHist(img)         #只能傳入灰階圖
res = np.hstack((img, equ))           #影像列拼接(用於顯示)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()