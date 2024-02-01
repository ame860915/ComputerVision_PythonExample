from PIL import Image
from pylab import *
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager

plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False

figure()    #畫布的唯一標記，如果不指定 num，每次執行 figure() 方法時會自動增加 1，表示會產生新的畫布。
pil_im = Image.open(r"D:\pyrhon_test\1.Common Libraries\Lenna.bmp")
gray()
subplot(121)    #在同一張圖片裡建立多個子圖表
title('原圖')
axis('off')
imshow(pil_im)
pil_im = Image.open(r"D:\pyrhon_test\1.Common Libraries\Lenna.bmp").convert('L')
subplot(122)
title('灰階圖')
axis('off')
imshow(pil_im)
show()