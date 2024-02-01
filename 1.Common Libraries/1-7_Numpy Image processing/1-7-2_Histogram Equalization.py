from PIL import Image
from numpy import * 
from pylab import * 
from PCV.tools import imtools
import matplotlib.pyplot as plt

#增加中文字型支援
#from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False

im = array(Image.open(r"D:\pyrhon_test\1.Common Libraries\Lenna.bmp").convert('L'))
#打開圖形，並轉成灰階圖形
im2,cdf = imtools.histeq(im)
figure()
subplot(2,2,1)
axis('off')
gray()
title(u'原始圖形')
imshow(im)
subplot(2,2,2)
axis('off')
title(u'原始長條圖')
hist(im.flatten(),128,density=True)
subplot(2,2,4)
axis('off')
title(u'均衡化後的長條圖')
hist(im2.flatten(),128,density=True)
show()