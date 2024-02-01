import cv2
import numpy as np 

original_img = cv2.imread(r"D:\pyrhon_test\3.Morphological Noise Reduction\DE_test.bmp", 0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))      #定義矩形結構元素

#閉合運算1
closed1 = cv2.morphologyEx(original_img,cv2.MORPH_CLOSE, kernel, iterations=1)
#閉合運算2
closed2 = cv2.morphologyEx(original_img,cv2.MORPH_CLOSE, kernel, iterations=3)
#段開運算1
opened1 = cv2.morphologyEx(original_img,cv2.MORPH_OPEN, kernel, iterations=1)
#斷開運算2
opened2 = cv2.morphologyEx(original_img,cv2.MORPH_OPEN, kernel, iterations=3)

#梯度
gradient = cv2.morphologyEx(original_img, cv2.MORPH_GRADIENT, kernel)
#顯示以下侵蝕的影像
cv2.imshow('img', original_img)
cv2.imshow('Close1',closed1)
cv2.imshow('Close2',closed2)
cv2.imshow('Open1',opened1)
cv2.imshow('Open2',opened2)

cv2.waitKey(0)
cv2.destroyAllWindows()