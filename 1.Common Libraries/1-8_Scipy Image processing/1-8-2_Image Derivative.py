from PIL import Image
from pylab import * 
#from scipy.ndimage import filters
'''
这个警告意味着你在使用 scipy.ndimage.filters 命名空间中的 sobel 函数，而这个命名空间已经被标记为弃用（deprecated）。
为了避免这个警告，建议使用 scipy.ndimage 命名空间中的 sobel 函数。
'''
from scipy.ndimage import sobel
import numpy
plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False

im = array(Image.open(r"Lenna.bmp").convert('L'))
gray()
subplot(141)
suptitle('導數操作(Sobel)', fontsize=16)
axis('off')
title('(a)原圖')
imshow(im)

#sobel運算
imx = zeros(im.shape)
#filters.sobel(im, 1, imx)  #sobel函數不再先import filters
sobel(im, 1, imx)
subplot(142)
axis('off')
title('(b)x方向差分')
imshow(imx)

imy = zeros(im.shape)
#filters.sobel(im, 0, imy)  ##scipy.ndimage不再先import filters
sobel(im, 1, imy)   
subplot(143)
axis('off')
title('(c)y方向差分')
imshow(imy)

mag = 255 - numpy.sqrt(imx**2 + imy**2)
subplot(144)
title('(d)梯度強度')
axis('off')
imshow(mag)
show()
#-----------------------------------------
from scipy.ndimage import filters
def Imx(im, sigma):
    imgx = zeros(im.shape)
    filters.gaussian_filter(im, sigma, (0,1), imgx)
    return imgx
def Imy(im, sigma):
    imgy = zeros(im.shape)
    filters.gaussian_filter(im, sigma, (1,0), imgy)
    return imgy
def Mag(im, sigma):
    #還有gaussian_gradient_magnitude()
    imgmag = 255 - numpy.sqrt(imgx**2 + imgy**2)
    return imgmag

im = array(Image.open(r"Lenna.bmp").convert('L'))
figure()
gray()
sigma = [2, 5, 10]
suptitle('高斯差分', fontsize=16)

for i in sigma:
    subplot(3, 4, 4*(sigma.index(i)) + 1)
    axis('off')
    imshow(im)

    imgx = Imx(im, i)
    subplot(3, 4, 4*(sigma.index(i)) + 2)
    axis('off')
    imshow(imgx)

    imgy = Imy(im, i)
    subplot(3, 4, 4*(sigma.index(i)) + 3)
    axis('off')
    imshow(imgy)

    imgmag = Mag(im, i)
    subplot(3, 4, 4*(sigma.index(i)) + 4)
    axis('off')
    imshow(imgy)

show()
