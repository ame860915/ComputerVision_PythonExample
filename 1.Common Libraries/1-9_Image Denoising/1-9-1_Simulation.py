from PIL import Image
from pylab import *
from numpy import * 
from numpy import random 
#from scipy.ndimage import filters
from scipy.ndimage import gaussian_filter
#from scipy.misc import imsave
import imageio
from PCV.tools import rof
 

plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False
#創建合成圖型與雜訊
im = zeros((500, 500))
im[100:400, 100:400] = 128
im[200:300, 200:300] = 255
im = im + 30 * random.standard_normal((500, 500))

#roll()函數：循環捲動陣列中的元素，計算領域元素的差異。linalg.norm()函數可以衡量兩個陣列見得差異
U, T = rof.denoise(im, im)
G = gaussian_filter(im, 10)
figure()
gray()
subplot(1,3,1)
imshow(im)
#axis('equal)
axis('off')
title('原雜訊圖型')

subplot(1,3,2)
imshow(G)
#axis('equal)
axis('off')
title('高斯模糊後的圖型')

subplot(1,3,3)
imshow(U)
#axis('equal')
axis('off')
title('ROF降低雜訊的圖型')
show()