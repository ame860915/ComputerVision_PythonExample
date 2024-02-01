import cv2 as cv 
from matplotlib import pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False

#輸入影像，輸出提取的邊緣資訊
def my_sobel_sharpen(image):
    result_x = np.zeros(image.shape, dtype=np.int64)
    result_y = np.zeros(image.shape, dtype=np.int64)
    result = np.zeros(image.shape, dtype=np.int64)
    #確定拉普拉斯範本的形式
    my_model_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    my_model_y = np.array([[-1, 0, -1], [-2, 0, -2], [-1, 0, 1]])

    #計算每個像速點在經過高斯範本變換後的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(3):
                for jj in range(3):
                    #條件陳述式為判斷範本對應的值是否超出邊界
                    if (i + ii - 1) < 0 or (i + ii - 1) >= image.shape[0]:
                        pass
                    elif (j + jj - 1) < 0 or (j + jj - 1) >= image.shape[1]:
                        pass
                    else:
                        result_x[i][j] += image[i + ii - 1][j + jj - 1] * my_model_x[ii][jj]
                        result_y[i][j] += image[i + ii - 1][j + jj - 1] * my_model_y[ii][jj]

            result[i][j] = abs(result_x[i][j]) + abs(result_y[i][j])
            
            if (result[i][j]).any() > 255:
                result[i][j] = 255
    return result

#將邊緣資訊按一定比例加到原始影像上
def my_result_add(image, model, k):
    result = image + k * model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if (result[i][j]).any() > 255:
                result[i][j] = 255
            if (result[i][j]).any() < 0:
                result[i][j] = 0
    return result

if __name__ == '__main__':

    '''讀取原始影像'''
    original_image_test1 = cv.imread(r"D:\pyrhon_test\1.Common Libraries\Lenna.bmp", 0)
    original_image_test2 = cv.cvtColor(original_image_test1, cv.COLOR_BGR2RGB)    #cv通道為BGR，但plt.show讀取為RGB

    
    #獲得影像邊界資訊
    edge_image = my_sobel_sharpen(original_image_test2)

    #獲得銳化影像
    sharpen_image = my_result_add(original_image_test2, edge_image, -0.5)

    #顯示結果
    plt.subplot(131)
    plt.title('原始影像')
    plt.imshow(original_image_test2)

    plt.subplot(132)
    plt.title('邊緣檢測')
    plt.imshow(edge_image)

    plt.subplot(133)
    plt.title('梯度處理')
    plt.imshow(sharpen_image)

    plt.show()