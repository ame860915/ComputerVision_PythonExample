import cv2
import numpy as np 

original_img = cv2.imread(r"D:\pyrhon_test\3.Morphological Noise Reduction\DE_test.bmp")
#res = cv2.resize(original_img, None, fx=0.6, fy=0.6, interpolation = cv2.INTER_CUBIC)   #影像太大，進行縮小(可依影像進行註解與否)
if original_img is None:
    print("無法讀取影像，請查明後重新輸入路徑")
else:
    B, G, R = cv2.split(original_img)


img = R
_,RedThresh = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)

#OpenCV定義的結構矩形元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
eroded = cv2.erode(RedThresh, kernel)            #侵蝕影像
dilated = cv2.dilate(RedThresh, kernel)        #膨脹影像

cv2.imshow('original_img', original_img)                  #原影像
cv2.imshow('R_channel_img', img)                 #紅色通道影像
cv2.imshow('RedThresh_img', RedThresh)           #紅色門檻值影像
cv2.imshow('Eroded_img', eroded)                 #顯示侵蝕後影像
cv2.imshow('Dilated_img', dilated)               #顯示膨脹後影像

#Numpy 定義的結構元素
NpKernel = np.uint8(np.ones((3, 3)))
Nperoded = cv2.erode(RedThresh, NpKernel)        #侵蝕影像
cv2.imshow('Erode by Numpy kernel', Nperoded)    #顯示侵蝕後的影像
cv2.waitKey(0)
cv2.destroyAllWindows()
