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

im = array(Image.open(r"Lenna.bmp").convert('L'))
U, T  = rof.denoise(im, im)
G = gaussian_filter(im, 10)

figure()
gray()
subplot(1,3,1)
imshow(im)
#axis('equal')
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