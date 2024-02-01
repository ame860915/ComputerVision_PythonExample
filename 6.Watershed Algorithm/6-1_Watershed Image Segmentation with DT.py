
'''
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import ndimage as ndi 
from skimage import  feature     #morphology中現在沒有watershed
from skimage.segmentation import watershed

plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False


#創建兩個帶有重疊圓的影像
x,y = np.indices((80, 80))
x1, y1, x2, y2 = 28, 28, 44, 52
r1, r2 = 16, 20
mask_circle1 = (x - x1)**2 + (y - y1)**2 < r1**2
mask_circle2 = (x - x2)**2 + (y - y2)**2 < r2**2
image = np.logical_or(mask_circle1, mask_circle2)

#現在我們利用分水嶺演算法分離兩個圓
distacne = ndi.distance_transform_edt(image)    #距離變換
print(distacne)
local_maxi = feature.peak_local_max(distacne, footprint=np.ones((5, 5)), labels=image)   #尋找峰值
print(local_maxi)
#markers = ndi.label(local_maxi)[0]              #初始標記點
markers = ndi.label(local_maxi)[0]  # 初始標記點
print(markers)

#以距離變換為基礎的分水嶺演算法
labels = watershed(-distacne, markers, mask=image)
#labels = watershed(-distacne, mask=image)
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))

axes = axes.ravel()
ax0, ax1, ax2, ax3 = axes
ax0.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax0.set_title('原始影像')
ax1.imshow(-distacne, cmap=plt.cm.jet, interpolation='nearest')
ax1.set_title('距離變換')
ax2.imshow(markers, cmap=plt.cm.Spectral, interpolation='nearest')
ax2.set_title('標記')
ax3.imshow(labels, cmap=plt.cm.Spectral, interpolation='nearest')
ax3.set_title('分割')
for ax in axes:
    ax.axis('off')
fig.tight_layout()

plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi

from skimage.segmentation import watershed
from skimage.feature import peak_local_max


# Generate an initial image with two overlapping circles
x, y = np.indices((80, 80))
x1, y1, x2, y2 = 28, 28, 44, 52
r1, r2 = 16, 20
mask_circle1 = (x - x1)**2 + (y - y1)**2 < r1**2
mask_circle2 = (x - x2)**2 + (y - y2)**2 < r2**2
image = np.logical_or(mask_circle1, mask_circle2)

# Now we want to separate the two objects in image
# Generate the markers as local maxima of the distance to the background
distance = ndi.distance_transform_edt(image)
coords = peak_local_max(distance, footprint=np.ones((3, 3)), labels=image)
mask = np.zeros(distance.shape, dtype=bool)
mask[tuple(coords.T)] = True
markers, _ = ndi.label(mask)
labels = watershed(-distance, markers, mask=image)
#print(distance)
print('1')
print(coords)
print('2')
print(coords.T)
print('3')

print(tuple(coords.T))
#print(mask)
#print(labels)


fig, axes = plt.subplots(ncols=3, figsize=(9, 3), sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title('Overlapping objects')
ax[1].imshow(-distance, cmap=plt.cm.gray)
ax[1].set_title('Distances')
ax[2].imshow(labels, cmap=plt.cm.nipy_spectral)
ax[2].set_title('Separated objects')

for a in ax:
    a.set_axis_off()

fig.tight_layout()
plt.show()
