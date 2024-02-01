from PIL import Image
from numpy import * 
from pylab import * 

im = array(Image.open(r"D:\pyrhon_test\1.Common Libraries\Lenna.bmp").convert('L'))
im2 = 255 - im
print('對圖形進行反向處理:\n', int(im2.min()), int(im2.max()))  #查看最大最小元素

im3 = (100.0/255)*im + 100  #將圖像像素值變化到100~200之間
print('將圖像像素值變換到100...200的區間:\n', int(im3.min()), int(im3.max()))

im4 = 255.0 * (im/255.0)**2     #對像素值平方後得到的圖形
print('對像素值求平方後得到的圖形:\n', int (im4.min()),int (im4.max()))
figure()
gray()
subplot(131)
imshow(im2)
axis('off')
title(r'$f(x)=255-x$')
subplot(132)
imshow(im3)
axis('off')
title(r'$f(x)=\frac{100}{255}x+100$')
subplot(133)
imshow(im4)
axis('off')
title(r'$f(x)=255(\frac{x}{255})^2$')
show()