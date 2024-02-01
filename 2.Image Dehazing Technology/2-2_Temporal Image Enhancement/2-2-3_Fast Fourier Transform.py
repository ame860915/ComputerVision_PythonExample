import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pylab import mpl

plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False

Fs = 1200;                                  #取樣頻率
Ts = 1 / Fs                                 #取樣區間
x = np.arange(0, 1, Ts)                     #時間向量，1200個
y = 5 * np.sin(2 * np.pi * 600 * x)
N = 1200
frq = np.arange(N)
half_x = frq[range(int(N / 2))]             #取一半區間
fft_y = np.fft.fft(y)
abs_y = np.abs(fft_y)                       #取複數的絕對值，即複數的模(雙邊頻譜)

angel_y = 180 * np.angle(fft_y) / np.pi     #取複數的弧度，並換算成角度
gui_y = abs_y / N                           #歸一化處理(雙邊頻譜)
gui_half_y = gui_y[range(int(N / 2))]       #由於對稱性，只取一半區間(單邊頻譜)

#畫出原始波形的前50個點
plt.subplot(231)
plt.plot(frq[0:50], y[0:50])
plt.title('原始波形')

#畫出雙邊未求絕對值的振幅譜
plt.subplot(232)
plt.plot(frq, fft_y, 'black')
plt.title('雙邊振幅譜(未求振幅絕對值)')

#畫出雙邊絕對值的振幅譜
plt.subplot(233)
plt.plot(frq, abs_y, 'r')
plt.title('雙邊振幅譜(未歸一化)')

#畫出雙邊相位譜
plt.subplot(234)
plt.plot(frq[0:50], angel_y[0:50], 'violet')
plt.title('雙邊相位譜(未歸一化)')

#畫出雙邊振幅譜(歸一化)
plt.subplot(235)
plt.plot(frq, gui_y, 'g')
plt.title('雙邊振幅譜(歸一化)')

#畫出單邊振幅譜(歸一化)
plt.subplot(236)
plt.plot(half_x, gui_half_y, 'blue')
plt.title('單邊振幅譜(歸一化)')

plt.show()