2-4_長條圖均衡化去霧技術
利用長條圖均衡化實現影像去霧處理，也稱為色階調整(Levels Adjustment)處理，下面介紹兩種原理及演算法

-----------------------------------------
2-4-1_Principle of Tone Adjustment(色階調整原理)
功能：色階即是利用長條圖描述出整張影像的明暗資訊
利用cv2.equalizeHist(img)函數實現

-----------------------------------------
2-4-2_Automatic Color Grading(自動色階影像處理演算法)
=>長條圖均衡後有改，但導致亮度過高。因此使用自我調整長條圖均衡
利用cv2.creatCLAHE()函數實現

-----------------------------------------
2-4-3_Numpy Optimized Dehazing Technique(numpy最佳化去霧技術的演算法)
