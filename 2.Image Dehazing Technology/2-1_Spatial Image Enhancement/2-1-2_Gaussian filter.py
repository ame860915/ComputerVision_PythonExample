import cv2 as cv 
import matplotlib.pyplot as plt
import math
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False

#高斯濾波函數
def my_function_gaussion(x, y, sigma):
    return math.exp(-(x**2 + y**2) / (2 * sigma * 2)) / (2 * math.pi * sigma**2)
#產生高斯濾波矩陣
def my_get_gaussion_blur_retric(size, sigma):
    n = size // 2
    blur_retric = np.zeros([size, size])
    #根據尺寸和sigma值計算高斯矩陣
    for i in range(size):
        for j in range(size):
            blur_retric[i][j] = my_function_gaussion(i-n, j-n, sigma)
    
    #高斯矩陣歸一化
    blur_retric = blur_retric / blur_retric[0][0]
    #將高斯矩陣轉為整數
    blur_retric = blur_retric.astype(np.uint32)
    #返回高斯矩陣
    return blur_retric

#計算灰階影像的高斯濾波
def my_gaussion_blur_gray(image, size, sigma):
    blur_retric = my_get_gaussion_blur_retric(size, sigma)
    n = blur_retric.sum()
    sizepart = size // 2
    data = 0
    #計算每個像素點在經過高斯範本轉換後的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(size):
                for jj in range(size):
                    #條件陳述式為判斷範本對應的值是否超出邊界
                    if(i + ii -sizepart) < 0 or  (i + ii + sizepart) >= image.shape[0]:
                        pass
                    elif(j + jj -sizepart) < 0 or  (j + jj + sizepart) >= image.shape[1]:
                        pass
                    else:
                        data += image[i + ii - sizepart][j + jj - sizepart] * blur_retric[ii][jj]
            image[i][j] = data / n
            data = 0

    #返回變換後的影像陣列
    return image

#計算彩色影像的高斯濾波
def my_gaussion_blur_RGB(image, size, sigma):
    (b, g, r) = cv.split(image)
    blur_b = my_gaussion_blur_gray(b, size, sigma)
    blur_r = my_gaussion_blur_gray(r, size, sigma)
    blur_g = my_gaussion_blur_gray(g, size, sigma)
    result = cv.merge((blur_b, blur_g, blur_r))
    return result

if __name__ == '__main__':
    image_test1 = cv.imread(r"D:\pyrhon_test\2.Image Dehazing Technology\image.bmp")
    image_test2 = cv.cvtColor(image_test1, cv.COLOR_BGR2RGB)    #cv通道為BGR，但plt.show讀取為RGB
    #進行高斯濾波器比較
    my_image_blur_gaussion = my_gaussion_blur_RGB(image_test2, 5, 0.75)
    computer_image_blur_gaussion = cv.GaussianBlur(image_test2, (5, 5), 0, 0.75)

    fig = plt.figure()

    fig.add_subplot(131)
    plt.title('原圖')
    plt.imshow(image_test2)

    fig.add_subplot(132)
    plt.title('自訂高斯濾波')
    plt.imshow(my_image_blur_gaussion)

    fig.add_subplot(133)
    plt.title('函數庫高斯濾波器')
    plt.imshow(computer_image_blur_gaussion)

    plt.show()