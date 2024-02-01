import cv2 as cv 
import matplotlib.pyplot as plt
import math
import numpy as np


plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False

original_image_test1 = cv.imread(r"D:\pyrhon_test\2.Image Dehazing Technology\image.bmp", 0)
original_image_test2 = cv.cvtColor(original_image_test1, cv.COLOR_BGR2RGB)    #cv通道為BGR，但plt.show讀取為RGB

#用原始影像減去拉普拉斯範本直接計算得到的邊緣資訊
def my_laplace_result_add(image, model):
    result = image - model
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if (result[i][j]).any() > 255:
                result = 255
            if (result[i][j]).any() < 0:
                result = 0
    return result

def my_laplace_sharpen(image, my_type = 'small'):
    result = np.zeros(image.shape, dtype = np.int64)
    #確定拉普拉斯的範本形式
    if my_type == 'small':
        my_model = np.array([[0, 1, 0], [-1, 4, -1], [0, 1, 0]])
    else:
        my_model = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

    #計算每個像素點在經過拉普拉斯範本變換後的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(3):
                for jj in range(3):
                    #條件陳述式為判斷範本對應的值是否超出邊界 
                    if(i + ii - 1) < 0 or  (i + ii + 1) >= image.shape[0]:
                        pass
                    elif(j + jj - 1) < 0 or  (j + jj + 1) >= image.shape[1]:
                        pass
                    else:
                        result[i][j] += image[i + ii - 1][j + jj - 1] * my_model[ii][jj]
    return result

#將計算結果限制為正值
def my_show_edge(model):
    #這裡一定要用copy函數，不然會改變原本陣列
    mid_mode = model.copy()
    for i in range(mid_mode.shape[0]):
        for j in range(mid_mode.shape[1]):
            if (mid_mode[i][j]).any() < 0:
                mid_mode[i][j] = 0
            if (mid_mode[i][j]).any() > 255:
                mid_mode[i][j] = 255
    return mid_mode

#呼叫自訂函數
result = my_laplace_sharpen(original_image_test2, my_type = 'big')

#繪製結果
fig = plt.figure()

fig.add_subplot(131)
plt.title('原始影像')
plt.imshow(original_image_test2)

fig.add_subplot(132)
plt.title('邊緣檢測')
plt.imshow(my_show_edge(result))

fig.add_subplot(133)
plt.title('銳化處理')
plt.imshow(my_laplace_result_add(original_image_test2, result))

plt.show()