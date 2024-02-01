import cv2 as cv 
import matplotlib.pyplot as plt
import math
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False


def get_meadian(data):
    data.sort()
    half = len(data) // 2
    return data[half]  

def my_median_blur_gray(image, size):
    data = []   
    sizepart = int(size / 2)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(size): 
                for jj in range(size):
                    #首先判斷是否超出範圍，也可以先對影像進行零填充
                    if(i + ii - sizepart) < 0 or (i + ii - sizepart) >= image.shape[0]:
                        pass
                    elif(j + jj - sizepart) < 0 or (j + jj -sizepart) >= image.shape[1]:
                        pass
                    else:
                        data.append(image[i + ii - sizepart][j + jj - sizepart])
    
            #取得每個區域內的中位數
            image[i][j] = int(get_meadian(data))
            data = []

    return image

#計算彩色影像的中值濾波
def my_median_blur_RGB(image, size): 
    (b, g, r) = cv.split(image)
    blur_b = my_median_blur_gray(b, size)
    blur_r = my_median_blur_gray(r, size)
    blur_g = my_median_blur_gray(g, size)
    result = cv.merge((blur_b, blur_g, blur_r))
    return result

if __name__ == '__main__':
    image_test1 = cv.imread(r"D:\pyrhon_test\2.Image Dehazing Technology\image.bmp")
    image_test2 = cv.cvtColor(image_test1, cv.COLOR_BGR2RGB)    #cv通道為BGR，但plt.show讀取為RGB

    fig = plt.figure()

    #呼叫自訂函數
    my_image_blur_median = my_median_blur_RGB(image_test2, 3)
    #呼叫函數庫函數
    computer_image_blur_median = cv.medianBlur(image_test2, 3)

    fig.add_subplot(131)
    plt.title('原圖')
    plt.imshow(image_test2)

    fig.add_subplot(132)
    plt.title('自訂函數濾波')
    plt.imshow(my_image_blur_median)

    fig.add_subplot(133)
    plt.title('函數庫函數濾波')
    plt.imshow(computer_image_blur_median)
    
    plt.show()
