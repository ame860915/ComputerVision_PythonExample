import numpy as np
from matplotlib import pyplot as plt
import cv2

plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False

img = cv2.imread(r"D:\pyrhon_test\1.Common Libraries\Lenna.bmp", 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(cv2.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1])))
plt.subplot(121)
plt.imshow(img, cmap = 'gray')
plt.title('原始影像')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('級頻譜')
plt.xticks([])
plt.yticks([])
plt.show()