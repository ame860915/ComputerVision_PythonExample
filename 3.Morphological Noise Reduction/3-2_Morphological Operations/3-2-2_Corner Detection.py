import cv2

image = cv2.imread(r"D:\pyrhon_test\2.Image Dehazing Technology\Lenna.bmp", 0)
original_img = image.copy()

#構造5*5的結構元素，分別為十字形、菱形、方形 和 X形
cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
diamond = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
diamond[0, 0] = 0
diamond[0, 1] = 0
diamond[1, 0] = 0
diamond[4, 4] = 0
diamond[4, 3] = 0
diamond[3, 4] = 0
diamond[4, 0] = 0
diamond[4, 1] = 0
diamond[3, 0] = 0
diamond[0, 3] = 0
diamond[0, 4] = 0
diamond[1, 4] = 0

square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  #構造方形結構元素
x = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

dilate_cross_img = cv2.dilate(image, cross)                 #使用cross膨脹影像
erode_diamond_img = cv2.erode(dilate_cross_img, diamond)    #使用菱形侵蝕影像

dilate_x_img = cv2.dilate(image, x)                         #使用X膨脹原影像
erode_squre_img = cv2.erode(dilate_x_img, square)           #使用方形侵蝕影像

#將兩幅斷開運算的影像相減獲得角
result = cv2.absdiff(erode_squre_img, erode_diamond_img)
#使用門檻值獲得二值化影像
retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY)
#在原影像用半徑為5的圓圈將點標出
for j in range(result.size):
    y = int(j / result.shape[0])
    x = int(j % result.shape[0])
    if result[x, y] == 255:     #result[] 只能傳入整數
        cv2.circle(image, (y, x), 5, (255, 0, 0))

cv2.imshow('original_img', original_img)
cv2.imshow('Result', image)

cv2.waitKey(0)
cv2.destroyAllWindows()