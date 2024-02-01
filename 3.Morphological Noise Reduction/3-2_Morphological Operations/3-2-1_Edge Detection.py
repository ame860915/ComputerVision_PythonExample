import cv2
import numpy 

image = cv2.imread(r"D:\pyrhon_test\2.Image Dehazing Technology\Lenna.bmp", cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilate_img = cv2.dilate(image, kernel)
erode_img = cv2.dilate(image, kernel)

'''
將兩幅影像相減獲得邊; cv2.absdiff參數：(膨脹後的影像，侵蝕後的影像)
上面得到的結果是灰階圖，將其二值化以便觀察結果
反色，對二值化影像中每個像素值進行反轉
'''

absdiff_img = cv2.absdiff(dilate_img, erode_img)
retval, threshold_img = cv2.threshold(absdiff_img, 40, 255, cv2.THRESH_BINARY)
result = cv2.bitwise_not(threshold_img)
cv2.imshow('img',image)
cv2.imshow('dilate',dilate_img)
cv2.imshow('erode',erode_img)
cv2.imshow('absdiff_img',absdiff_img)
cv2.imshow('threshold_img',threshold_img)
cv2.imshow('result',result)

cv2.waitKey(0)
cv2.destroyAllWindows()