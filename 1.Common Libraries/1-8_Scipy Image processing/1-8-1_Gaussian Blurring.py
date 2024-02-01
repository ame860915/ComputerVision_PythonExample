from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False

#讀取圖形至陣列中
im = array(Image.open(r"D:\pyrhon_test\1.Common Libraries\Lenna.bmp").convert('L'))
figure()
gray()
axis('off')
subplot(141)
axis('off')
title('原圖')
imshow(im)

for bi, blur in enumerate([2, 4, 8]):
    im2 = zeros(im.shape)
    im2 = filters.gaussian_filter(im, blur)
    im2 = np.uint8(im2)
    imNum = str(blur)
    subplot(1, 4, 2 + bi)
    axis('off')
    title(u'標準差為' + imNum)
    imshow(im2)

#如果是色彩模型，則分別對三個通道進行模糊
# for bi, blur in enumerate([2, 4, 8]);
#     im2 = zeros(im.shape)
#     for i in range(3):
#         im2[:, :, 1] = filters.gaussian_filter(im[:, :, i], blur)
#     im2 = np.uint8(im2)
#     subplot(1, 4, 2 + bi)
#     axis('off')
#     imshow(im2)
    
show()