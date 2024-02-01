import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False

img = plt.imread(r"D:\pyrhon_test\1.Common Libraries\Lenna.bmp", 0)
#根據公式轉成灰階圖
img = 0.2126 * img[:,:,0] + 0.7152 * img[:,:,1] + 0.0722 *  img[:,:,2]

#顯示原始影像
plt.subplot(231)
plt.imshow(img, 'gray')
plt.title('原始影像')

#進行傅立葉轉換，並顯示結果
fft2 = np.fft.fft2(img)
plt.subplot(232)
plt.imshow(np.abs(fft2), 'gray')
plt.title('二維傅立葉轉換')

#將影像變換的原點移動到頻域矩形的中心，並顯示結果
shift2center = np.fft.fftshift(fft2)
plt.subplot(233)
plt.imshow(np.abs(shift2center), 'gray')
plt.title('頻域矩形的中心')

#對傅立葉轉換的結果進行對數轉換，並顯示結果
log_fft2 = np.log(1 + np.abs(fft2))
plt.subplot(235)
plt.imshow(log_fft2, 'gray')
plt.title('傅立葉轉換對數變換')

#對中心化後的結果進行對數變換，並顯示結果
log_shift2center = np.log(1 + np.abs(shift2center))
plt.subplot(236)
plt.imshow(log_shift2center, 'gray')
plt.title('中心化的對數變化')
plt.show()

