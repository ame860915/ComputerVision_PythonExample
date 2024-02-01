from PIL import Image
from numpy import * 
#measurement模組 實現二值圖形的計數和度量功能，morphology模組實現形態學操作
from scipy.ndimage import measurements,morphology
from scipy.ndimage import label
from scipy.ndimage import binary_opening
'''
这个警告意味着你在使用 scipy.ndimage.measurements,morphology 命名空间中的 label 函数 和 binary_opening，而这个命名空间已经被标记为弃用（deprecated）。
为了避免这个警告，建议使用 scipy.ndimage 命名空间中的 label 函数 和 binary_opening。
'''
from pylab import * 

plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False

#載入圖型和閾值，以確保它是二進位
figure()
gray()
im = array(Image.open(r"Lenna.bmp").convert('L'))
subplot(221)
imshow(im)
axis('off')
title('原圖')

im = (im <128)
labels, nbr_objects = label(im) #圖型的灰階值表示霧見的標籤
print('Numer of objects : ', nbr_objects)
subplot(222)
imshow(labels)
axis('off')
title('標記後的圖')

#形態學--使物體分離更好
im_open = binary_opening(im, ones((9, 5)), iterations = 4)   #開操作，第二個參數為結構元素，iteration決定執行該操作的次數
subplot(223)
imshow(im_open)
axis('off')
title('開運算後的圖型')
labels_open, nbr_pbjects_open = label(im_open)
print('Numer of objects : ', nbr_pbjects_open)
subplot(224)
imshow(labels_open)
axis('off')
title('開運算後進行標記的圖型')
show()