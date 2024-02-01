Numpy 影像處理 
在前面幾節程式範例，圖形利用array()函數轉為Numpy陣列物件，但未提及表示的含義

使用陣列切片存取，返回的是指定間隔索引，存取該陣列的元素直：
im[i,:] = im[j,:]   #將第j行的數值設定值給第i行
im[:,j] = 100       #將第j列所有值設定為100
im[:100,:50].sum()  #計算前100行、前50列所有數值的和
im[50:100,50:100]   #50~100行，50~100列，不包刮第100行和100列
im[i].mean()        #第i行所有數值的平均值
im[:,-1]            #最後一列
im[-2,:]/im[-2]     #倒數第二行
-----------------------------------------
1-7-1_Gray transformation
功能：設置任意函數f，將0~255映射到自身，也就是輸出區間與輸入區間相同
ex:(1)f(x)=255-x    (2)f(x)=(100/255)*x + 100  (3)f(x)=255(x/255)^2
-----------------------------------------
1-7-2_Histogram Equalization
功能：將灰階長條圖變平，使圖形中每個灰階值的分布機率都相同
***(搞了一整個下午==)(2023/12/29)***
事前作業
PCV函數庫下載(不能用pip install PCV)，參考網址：
https://www.twblogs.net/a/5d7ec239bd9eee541c347ce4
https://blog.csdn.net/weixin_42578378/article/details/88617207  # =>更詳細一點，python3.多版本的記得做些更改，下載壓縮檔後要記得修改，文章裡都有寫

PCV壓縮檔的setup.py檔案中，distutils要改成setuptools函數，因為distutils在python3.12版本已經刪除。
https://docs.python.org/zh-tw/3.10/library/distutils.html

***以上完成還有錯誤***
C:\Users\'使用者'\AppData\Local\Programs\Python\Python312\Lib\site-packages\PCV\tools\imtools.py 程式第55行，
normed參數在外來版本的numpy中刪除，因此用density關鍵字作替代。
https://blog.csdn.net/weixin_43890415/article/details/114498415
-----------------------------------------
1-7-3_Image Averaging
功能：圖形平均為降低雜訊的簡單方法
書本上無註解，原圖輸入及暗通道可以順利找顯示出來，但去霧函數出錯導致最終影像變為全暗
-----------------------------------------
1-7-4 PCV(Principal Componenet Analysis) 
功能:主成份分析，減少維度的前提下，盡可能保持資料的資訊 => 影像100*100，有10000維，PCV能轉換成一維以降低複雜度
