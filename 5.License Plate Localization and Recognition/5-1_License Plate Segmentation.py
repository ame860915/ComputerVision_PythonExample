
import cv2
'''讀取影像，並把影像轉為灰階影像並顯示'''
img = cv2.imread(r'D:\pyrhon_test\5.License Plate Localization and Recognition\License Plate4.bmp')     #讀取影像
#img = cv2.imread('License Plate1.bmp')              
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #轉換灰階影像
cv2.imshow('gray', img_gray)                        #顯示影像
cv2.waitKey(0)

'''將灰階影像二值化，設定門檻值為100'''
img_thre = img_gray
cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV,img_thre)
cv2.imshow('thresold', img_thre)
cv2.waitKey(0)

'''保存黑白影像'''
success = cv2.imwrite(r'D:\pyrhon_test\5.License Plate Localization and Recognition\thre_res.bmp', img_thre)
if success:
    print("保存成功")
else:
    print("保存失敗")

'''分割字元'''
white = []              #記錄每一列的白色像素總和
black = []              #黑色
height = img_thre.shape[0]
width = img_thre.shape[1]
white_max = 0
black_max = 0

#計算每列的黑白色像素總和
for i in range(width):
    s = 0   #這一列白色總和
    t = 0   #這一列黑色總和
    for j in range(height):
        if img_thre[j][i] == 255:
            s += 1
        if img_thre[j][i] == 0:
            t += 1 
    white_max = max(white_max, s)
    black_max = max(black_max, t)
    white.append(s)
    black.append(t)
    print(s)
    print(t)

arg = False #False表示白底黑字; True表示黑底白字
if black_max > white_max:
    arg = True

#分割影像
def find_end(start_):
    end_ = start_ + 1
    for m in range(start_ + 1, width - 1):
        if(black[m] if arg else white[m]) > (0.95 * black_max if arg else 0.95 * white_max): #0.95這個參數可以多調整，對應下面的0.05
            end_ = m 
            break
    return end_

n = 1
start = 1 
end = 2
while n < width - 2:
    n += 1
    if(white[n] if arg else black[n]) > (0.05 * white_max if arg else 0.05 * black_max):
        #上面這些判斷用來辨別是 白底黑字或是黑底白字
        #0.05這個參數可調整，對應上面的0.95
        start = n
        end = find_end(start)
        n = end
        if end - start > 5:
            cj = img_thre[1:height, start:end]
            cv2.imshow('caijian', cj)
            cv2.waitKey(0)