import cv2 as cv 
from matplotlib import pyplot as plt
import numpy as np

#用原始影像減去拉普拉斯範本直接計算得到的邊緣資訊
def my_laplace_result_add(image, model):
    result = image - model
    #result = np.clip(result, 0, 255)
    print('x = ',result.shape[0])
    print('y = ',result.shape[1])
    print(type(result))
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if (result[i][j]).any() > 255:
                result[i][j] = 255
            if (result[i][j]).any() < 0:
                result[i][j] = 0
    return result

original_image_test1 = cv.imread(r"D:\pyrhon_test\2.Image Dehazing Technology\image.bmp")
original_image_test2 = cv.cvtColor(original_image_test1, cv.COLOR_BGR2RGB)    #cv通道為BGR，但plt.show讀取為RGB

#函數中的參數ddepth 為輸出影像的深度，也就是每個像素點式多少位元的
computer_result = cv.Laplacian(original_image_test2, ksize=3, ddepth=cv.CV_16S)
plt.imshow(my_laplace_result_add(original_image_test2, computer_result))
plt.show()