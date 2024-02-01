import numpy as np 
import cv2
import matplotlib.pyplot as plt

#自我調整中值濾波
# count 為最大視窗數，orinial 為原影像

def adaptiveMedianDeNoise(count, original):
    #初始視窗大小
    startWindow = 3
    #卷積範圍
    c = int(count / 2)
    rows, cols = original.shape
    newI = np.zeros(original.shape)
    for i in range(c, rows - c):
        for j in range(c, cols - c):
            k = int(startWindow / 2)
            median = np.median(original[i-k : i+k+1, j-k : j+k+1])
            mi = np.min(original[i-k : i+k+1, j-k : j+k+1])
            ma = np.max(original[i-k : i+k+1, j-k : j+k+1])
            if mi < median < ma :
                if mi < original < ma :
                    newI =[i, j] = original[i, j]
                else:
                    while True:
                        startWindow = startWindow + 2
                        k = int(startWindow / 2)
                        median = np.median(original[i-k : i+k+1, j-k : j+k+1])
                        mi = np.min(original[i-k : i+k+1, j-k : j+k+1])
                        ma = np.max(original[i-k : i+k+1, j-k : j+k+1])

                        if mi < median < ma or startWindow > count:
                            break
                    if mi < median < ma or startWindow > count:
                        if mi < original[i, j] < ma :
                            newI[i, j] = original[i, j]
                        else:
                            newI[i, j] = median
    return newI

def medianDeNoise(original):
    rows, cols = original.shape
    ImageDenoise = np.zeros(original.shape)
    for i in range(3, rows - 3):
        for j in range(3, cols - 3):
            ImageDenoise[i, j] = np.median(original[i-3 : i+4, j-3 : j+4])

    return ImageDenoise

def main():
    original  = plt.imread(r"D:\pyrhon_test\2.Image Dehazing Technology\Lenna.bmp", 0)
    rows, cols = original.shape
    original_noise = pepperNoise(10000, original)
    adapMedianDeNoise = adaptiveMedianDeNoise(7, original_noise)
    mediaDeNosie = medianDeNoise(original_noise)
    
    plt.figure()
    plt.show(original, '原始影像', 2, 2, 1)
    plt.show(original_noise, '帶雜訊影像', 2, 2, 2)
    plt.show(adapMedianDeNoise, '自我調整中值去除雜訊', 2, 2, 3)
    plt.show(original, '平均值去除雜訊', 2, 2, 4)
    plt.show()