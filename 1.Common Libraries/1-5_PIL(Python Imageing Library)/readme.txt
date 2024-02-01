PIL(Python Image Library)影像處理函數庫
提供通用的影像處理功能，以及大量的基本圖形操作。
PIL函數庫已經整合在Anaconda函數庫中，推薦使用Anaconda，簡單方便且快捷。
其功能：
1.主要定義在Image類別當中，一班都是從建立一個Image類別的實力開始
-----------------------------------------
PIL函數庫下載為 => pip install Pillow
pylab函數庫下載為 => pip install matplotlib
無法顯示中文(解決方法)：https://medium.com/marketingdatascience/%E8%A7%A3%E6%B1%BApython-3-matplotlib%E8%88%87seaborn%E8%A6%96%E8%A6%BA%E5%8C%96%E5%A5%97%E4%BB%B6%E4%B8%AD%E6%96%87%E9%A1%AF%E7%A4%BA%E5%95%8F%E9%A1%8C-f7b3773a889b
使用import * => 代表可以直接使用其導入模組名稱，不必再額外創建變數名稱
-----------------------------------------
1-5-1_Gray
功能：彩圖轉成灰階圖
Figure()，參數教學網：
https://steam.oxxostudio.tw/category/python/example/matplotlib-figure.html
subplot()，參數教學網：
https://steam.oxxostudio.tw/category/python/example/matplotlib-subplot.html
-----------------------------------------
1-5-2_Convert Image Format
功能：將Lenna.bmp轉為Lenna.jpj
str,rsplit()，參數教學網：
https://www.cnblogs.com/wushuaishuai/p/7792874.html
-----------------------------------------
1-5-3_Thum_Copy_Resi_Rota
縮圖(Thumbnail)、拷貝(Copy)、調整尺寸(Resize)和旋轉(Rotate)
