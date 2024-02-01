from PIL import Image
from pylab  import * 
import matplotlib.pylab as plt

plt.rcParams['font.sans-serif'] = ['SimHei'] #顯示中文標籤
plt.rcParams['axes.unicode_minus'] = False

#讀取圖形至陣列中
im = array(Image.open(r"D:\pyrhon_test\1.Common Libraries\Lenna.bmp"))
figure()

#繪製座標軸
subplot(121)
imshow(im)
x = [100,100,200,200]
y = [200,400,200,400]
#使用紅色星狀標記繪製點
plot(x,y,'r*')
#繪製連接兩個點的線(預設為藍色)
plot(x[:2],y[:2])
title(u'繪製Lenna.bmp')
#-----------------------------------------
#不顯示座標軸
subplot(122)
imshow(im)
x = [100,100,200,200]
y = [200,400,200,400]
plot(x,y,'r*')
plot(x[:2],y[:2])
axis('off')
title(u'繪製Lenna2.bmp')
show()      #show()命令 首先打開圖形化使用者介面(GUI)，然後建一個新視窗
#每個指令只能呼叫一次show()指令，且通常在結尾呼叫