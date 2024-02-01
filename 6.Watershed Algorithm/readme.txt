6.Watershed Algorithm(分水嶺演算法)

分水嶺演算法是一種影像分割法，分割過程中，它會把鄰近像速間的相似性作為重要參考依據，
封閉性式分水嶺演算法的重要特徵

https://zhuanlan.zhihu.com/p/67741538


-----------------------------------------
6-1_Watershed Image Segmentation with DT (距離變換的分水嶺影像分割)
距離變換的分水嶺分割：
尋找 匯水盆地 和 分水嶺界限，從而對影像進行分割，二值化影像的距離變換就是每一個像素點到最近非零值像素點的距離，
我們可以使用scipy套件計算距離變換

def peak_local_max(image, min_distance=1, threshold_abs=None,
                   threshold_rel=None, exclude_border=True,
                   num_peaks=np.inf, footprint=None, labels=None,
                   num_peaks_per_label=np.inf, p_norm=np.inf):

indices參數 已經棄用，將在版本 0.20 中刪除。默認行為是始終返回峰值坐標。您可以獲得一個掩碼，如下例所示。

-----------------------------------------
6-2_Watershed Image Segmentation with gradient (梯度的分水嶺影像分割)