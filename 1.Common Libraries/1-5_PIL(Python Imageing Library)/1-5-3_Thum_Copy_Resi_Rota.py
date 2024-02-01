from PIL import Image
from pylab import * 
plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False
figure()
#顯示原圖
pil_im = Image.open(r"Lenna.bmp")
print(pil_im.mode, pil_im.size,pil_im.format)
subplot(231)
title(u'原圖') 
axis('off')
imshow(pil_im)
#-----------------------------------------------
#顯示灰階圖
pil_im = pil_im.convert('L')
gray()
subplot(232)
title(u'灰階圖')
axis('off')
imshow(pil_im)
#-----------------------------------------------
#顯示縮圖
size = 128,128
pil_im_Thum = pil_im.copy()
pil_im_Thum.thumbnail(size)
print(pil_im_Thum.size)
subplot(234)
title(u'縮圖')
axis('off')
imshow(pil_im_Thum)
#pil_im_Thum.save(r'Lenna_Thum.bmp') #
#-----------------------------------------------
#複製並貼上區域
pil_im_Copy = pil_im.copy()
box = (100,100,200,200)
region = pil_im_Copy.crop(box)
region = region.transpose(Image.ROTATE_180)
pil_im_Copy.paste(region,box)
subplot(233)
title(u'複製並貼上區域')
axis('off')
imshow(pil_im_Copy)
#-----------------------------------------------
#調整圖型尺寸
pil_im_Resize = pil_im.copy()
size = 500,500
pil_im_Resize = pil_im_Resize.resize(size)
print(pil_im_Resize.size)
subplot(235)
title(u'調整尺寸後的圖型')
axis('off')
imshow(pil_im_Resize)
#-----------------------------------------------
#旋轉圖型45度
pil_im_Rotate = pil_im.copy()
pil_im_Rotate = pil_im_Rotate.rotate(45)
subplot(236)
title('旋轉45後的圖型')
axis('off')
imshow(pil_im_Rotate)
show()