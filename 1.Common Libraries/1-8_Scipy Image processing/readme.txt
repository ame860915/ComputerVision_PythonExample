Scipy 影像處理 
Scipy處理陣列相關操作非常便捷
其功能：
1.數值積分
2.最佳化
3.統計
4.訊號處理
5.**影像處理**

-----------------------------------------
1-8-1_Gaussian Blurring
功能：高斯圖型模糊化
其核心概念是將灰階影像與高斯核心進行卷積操作，
Scipy中利用filter實現濾波操作模組，快速分離成一維的分式來計算卷積

-----------------------------------------
1-8-2_Image Derivative
功能：導數為函數的局部性質，白話點就是變化量△，大多數圖型導術可用卷積來實現，ex:Prewitt、Sobel濾波器、高斯差分(Difference of Gaussians，簡稱「DOG」)

Prewitt濾波器 與 Sobel濾波器 差異:  =>就差在濾波器數字不相同，都是用來邊緣檢測
https://www.twblogs.net/a/5e704d27bd9eee2117c762c7

高斯差分(DOG):  =>被用來增加邊緣和其他細節的可見性，具體處理就是將兩幅影像在不同參數下的高斯濾波進行相減
https://blog.csdn.net/qq_28087491/article/details/120841764

-----------------------------------------
1-8-3_Morphology(形態學)
功能：為影像處理方法中度量和分析基本形狀的框架與集合