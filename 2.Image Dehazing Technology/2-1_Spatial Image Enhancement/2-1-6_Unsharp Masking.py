import cv2 as cv 
from matplotlib import pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False

#影像銳化函數
def my_not_sharpen(image, k, blur_size=(5, 5),blured_sigma=3):
    blured_image = cv.GaussianBlur(image, blur_size, blured_sigma)
    #注意不能直接用減法，對於影像格式結果為負時會自動加上256
    model = np.zeros(image.shape, dtype=np.int64)

    model = np.subtract(image, blured_image, dtype=np.int64)
    '''
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            model[i][j] = int(image[i][j]) - int(blured_image[i][j])
    '''
    
    #兩個矩陣中有一個不是影像格式，則結果就不會轉為影像格式
    sharpen_image = image + k * model
    sharpen_image = cv.convertScaleAbs(sharpen_image)
    return sharpen_image

#提取影像邊界資訊函數
def my_get_model(image, blur_size=(5, 5), blured_sigma=3):


    blured_image = cv.GaussianBlur(image, blur_size, blured_sigma)
    model = np.zeros(image.shape, dtype=np.int64)

    # 使用向量化操作，避免逐個處理數组元素
    model = np.subtract(image, blured_image, dtype=np.int64)
    
    model = cv.convertScaleAbs(model)
    #-------------------------------------------------
    '''
    blured_image = cv.GaussianBlur(image, blur_size, blured_sigma)
    model = np.zeros(image.shape, dtype=np.int64)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            model[i][j] = int(image[i][j]) - int(blured_image[i][j])
    model = cv.convertScaleAbs(model)
    '''
    return model

if __name__ == '__main__':
    '''讀取原始影像'''
    original_image_test1 = cv.imread(r"D:\pyrhon_test\2.Image Dehazing Technology\image.bmp", 0)
    original_image_test2 = cv.cvtColor(original_image_test1, cv.COLOR_BGR2RGB)    #cv通道為BGR，但plt.show讀取為RGB

    #獲得影像邊界資訊
    edge_image = my_get_model(original_image_test2)

    #獲得銳化影像
    sharpen_image = my_not_sharpen(original_image_test2, 3)

    #顯示結果
    plt.subplot(131)
    plt.title('原始影像')
    plt.imshow(original_image_test2)

    plt.subplot(132)
    plt.title('邊緣檢測')
    plt.imshow(edge_image)

    plt.subplot(133)
    plt.title('非銳化')
    plt.imshow(sharpen_image)

    plt.show()