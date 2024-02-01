import cv2
from matplotlib import pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False

original_image_test1 = cv2.imread(r"D:\pyrhon_test\1.Common Libraries\Lenna.bmp", 0)
original_image_test2 = cv2.cvtColor(original_image_test1, cv2.COLOR_BGR2RGB)    #cv通道為BGR，但plt.show讀取為RGB

#Canny()：邊緣檢測
img1 = cv2.GaussianBlur(original_image_test2, (3, 3), 0)
canny = cv2.Canny(img1, 50, 150)

#形態學：邊緣檢測
_, Thr_img = cv2.threshold(original_image_test2, 210, 255, cv2.THRESH_BINARY)   #設定為紅色，通道門檻值為210(門檻值影響梯度運算結果)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  #定義矩形結構元素
gradient = cv2.morphologyEx(Thr_img, cv2.MORPH_GRADIENT, kernel)    #梯度

cv2.imshow("原始影像",original_image_test2)
cv2.imshow("梯度",gradient)
cv2.imshow("Canny函數",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()