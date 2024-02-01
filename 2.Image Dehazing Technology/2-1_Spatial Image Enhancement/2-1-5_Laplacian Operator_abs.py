import cv2 as cv 
from matplotlib import pyplot as plt
import numpy as np
'''
import sys
sys.path.append('D:\pyrhon_test\2.Image Dehazing Technology\2-1_Spatial Image Enhancement\2-1-3_Laplacian_Operator.py')
from 2-1-3_Laplacian_Operator import my_laplace_sharpen
'''

plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False

original_image_test1 = cv.imread(r"D:\pyrhon_test\2.Image Dehazing Technology\image.bmp", 0)
original_image_test2 = cv.cvtColor(original_image_test1, cv.COLOR_BGR2RGB)    #cv通道為BGR，但plt.show讀取為RGB

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

def my_laplace_result_add_abs(image, model):
    for i in range(model.shape[0]):
        for j in range(model.shape[1]):
            if (model[i][j]).any() < 0:
                model[i][j] = 0
            if (model[i][j]).any() > 255:
                model[i][j] = 255

    result = image - model

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if (result[i][j]).any() > 255:
                result[i][j] = 255
            if (result[i][j]).any() < 0:
                result[i][j] = 0
    
    return result

#呼叫自訂函數my_laplace_sharpen，該函數在laplace.py檔案中定義
result = my_laplace_sharpen(original_image_test2, my_type='big')

#繪製結果
fig = plt.figure()

fig.add_subplot(121)
plt.title('原始影像')
plt.imshow(original_image_test2)

fig.add_subplot(122)
plt.title('銳化濾波')
plt.imshow(my_laplace_result_add_abs(original_image_test2, result))

plt.show()
