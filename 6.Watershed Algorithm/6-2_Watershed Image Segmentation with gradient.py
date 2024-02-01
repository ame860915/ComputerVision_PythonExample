import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import segmentation, morphology, color, data, filters

image = data.camera()

plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False

denosied = filters.rank.median(image, morphology.disk(2))       #過濾雜訊

#將梯度值低於10的作為開始標記點
markers = filters.rank.gradient(denosied, morphology.disk(5)) < 10
markers = ndi.label(markers)[0]

gradient = filters.rank.gradient(denosied, morphology.disk(2))  #計算梯度
labels = segmentation.watershed(gradient, markers, mask=image)  #以梯度為基礎的分水嶺驗算法

fig, axes =  plt.subplots(nrows=2, ncols=2, figsize=(6, 6))
axes = axes.ravel()
ax0, ax1, ax2, ax3 = axes
ax0.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax0.set_title('原始影像')
ax1.imshow(gradient, cmap=plt.cm.Spectral, interpolation='nearest')
ax1.set_title('梯度')
ax2.imshow(markers, cmap=plt.cm.Spectral, interpolation='nearest')
ax2.set_title('標記')
ax3.imshow(labels, cmap=plt.cm.Spectral, interpolation='nearest')
ax3.set_title('分割')

for ax in axes:
    ax.axis('off')
fig.tight_layout()

plt.show()