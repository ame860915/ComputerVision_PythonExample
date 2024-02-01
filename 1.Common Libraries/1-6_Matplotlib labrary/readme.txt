Matplotlib 函數庫是一套方便繪圖的函數庫，當在處裡數學及繪畫時其功能：
1.描點
2.畫直線、曲線
-----------------------------------------
輸出的圖形包括聚合線圖、散點圖、長條圖etc
資料視覺方面也能提供清晰且直觀的認知
-----------------------------------------
1-6-1_DrawPoint_Lien
功能：畫圖、描點和線
plot(x,y) 預設為藍色實線
plot(x,y,'go-') 帶有圓圈標記的線
plot(x,y,'ks:') 帶有正方形標記的黑色虛線
pylab函數庫的基本顏色，參考網站：
https://blog.csdn.net/weixin_39589455/article/details/124272116
-----------------------------------------
1-6-2_Contour_Barchat
功能：描繪輪廓及長條圖
contour()，參數教學網：
origin = 'image'    
#origin參數用於指定輪廓數據的原點位置
#'image'即(0,0)點，'upper'即上方，'lower'即下方，非左上角
https://blog.csdn.net/Dontla/article/details/98757783
-----------------------------------------
1-6-3_Interactive annotation
功能：互動式標注
使用ginput()函數