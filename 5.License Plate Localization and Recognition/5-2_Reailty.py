import cv2
import numpy as np 
from PIL import Image
import os.path
from skimage import io, data
def stretch(img):
    '''影像伸展函數'''
    maxi = float(img.max())
    mini = float(img.min())
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i, j] = (255 / (maxi - mini) * img[i, j] - (255 * mini) / (maxi - mini))
    return img

def dobinaryzation(img):
    '''二值化處理函數'''
    maxi = float(img.max())
    mini = float(img.min())
    x = maxi - ((maxi - mini) / 2)
    #二值化,返回門檻值ret 和二值化操作後的影像thresh
    ret, thresh = cv2.threshold(img, x, 255,cv2.THRESH_BINARY)
    #返回二值化後的黑白影像
    return thresh 

def find_rectangle(contour):
    '''尋找矩形輪廓'''
    y, x = []
    for p in contour:
        y.append(p[0][0])        
        x.append(p[0][1])
    return [min(y), min(x), max(y), max(x)]

def locate_license(img, afterimg):
    '''定位車牌號碼'''
    img, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #找出最大的三個區域
    block = []
    for c in contours:
        #找出輪廓的左上和右下點，由此計算它的面積和長度比
        r = find_rectangle(c)
        a = (r[2] - r[0]) * (r[3] - r[1])       #面積
        s = (r[2] - r[0]) * (r[3] - r[1])       #長度比
        block.append([r, a, s])
    
    #選出面積最大的3個區域
    block = sorted(block, key=lambda b:b[1])[-3:]
    #使用顏色辨識判斷找出最像車牌的區域
    maxweight, maxindex = 0, 1
    for i in range(len(block)):
        b = afterimg[block[i][0][1] : block[i][0][3], block[i][0][0] : block[i][0][2]]
        #BGR轉HSV
        hsv = cv2.cvtColor(b, cv2.COLOR_BGR2HSV)
        #藍色車牌的範圍
        lower = np.array([100, 50, 50])
        upper = np.array([140, 255, 255])
        #根據門檻值建構掩膜
        mask = cv2.inRange(hsv, lower, upper)
        #統計權值
        w1 = 0
        for m in mask:
            w1 += m /255
        w2 = 0
        for n in w1:
            w2 += n
        #選出最大權值的區域
        if w2 > maxweight:
            maxindex = i
            maxweight = w2
    return block[maxindex[0]]

def find_license(img):
    '''前置處理函數'''
    m = 400 * img.shape[0] / img.shape[1]
    #壓縮影像
    img = cv2.resize(img, (400, int(m)), interpolation=cv2.INTER_CUBIC)
    #BGR轉為灰階影像
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #灰階伸展
    stretchedimg = stretch(gray_img)
    '''進行閉合運算，用來去除雜訊'''
    r = 16
    h = w = r * 2 + 1
    kernel = np.zeros((h, w), np.uint8)
    cv2.circle(kernel, (r, r), r, 1, -1)
    #閉合運算
    openingimg = cv2.morphologyEx(stretchedimg,cv2.MORPH_OPEN, kernel)
    #獲取差分影像，兩幅影像進行相減 cv2.absdiff('影像1','影像2')
    strtimg = cv2.absdiff(stretchedimg, openingimg)
    #影像二值化
    binaryimg = dobinaryzation(strtimg)
    #canny邊緣檢測
    canny = cv2.Canny(binaryimg, binaryimg.shape[0], binaryimg.shape[1])
    '''消除小的區域，保留大區塊的區域，從而定位車牌'''
    #進行閉合運算
    kernel = np.ones((5, 19), np.uint8)
    openingimg = cv2.morphologyEx(canny, cv2.MORPH_CLOSE,kernel)
    #進行斷開運算
    openingimg = cv2.morphologyEx(canny, cv2.MORPH_OPEN,kernel)
    #再次進行斷開運算
    kernel = np.ones((11, 5), np.uint8)
    openingimg = cv2.morphologyEx(canny, cv2.MORPH_OPEN,kernel)
    #消除小區域，定位車牌位置
    rect = locate_license(openingimg, img)
    return rect, img

def cut_license(afterimg, rect):
    '''影像分割函數'''
    #轉為寬度和高度
    rect[2] = rect[2] - rect[0]
    rect[3] = rect[3] - rect[1]
    rect_copy = tuple(rect.copy())
    rect = [0, 0, 0, 0]
    #創建掩膜
    mask = np.zeros(afterimg.shape[:2], np.uint8)
    #創建背景膜型大小只能為13 * 5，行數只能為1，單通道浮點數
    bgdModel = np.zeros((1, 65), np.float64)
    #創建前景膜型
    fgdModel = np.zeros((1, 65), np.float64)
    #分割影像
    cv2.grabCut(afterimg, mask, rect_copy, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2) | (mask == 0), 0, 1).astype('uint8')
    img_show = afterimg * mask2[:, :, np.newaxis]
    return img_show

def deal_license(licenseimg):
    '''車牌影像二值化'''
    #車牌便為灰階影像
    gray_img = cv2.cvtColor(licenseimg, cv2.COLOR_BGR2GRAY)
    #均值濾波去雜訊
    kernel = np.ones((3, 3), np.float32) / 9
    gray_img = cv2.filter2D(gray_img - 1, kernel)
    #二值化處理
    ret, thresh = cv2.threshold(gray_img, 120, 255, cv2.THRESH_BINARY)
    return thresh

def find_end(start, arg, black, white, width, black_max, white_max):
    end = start + 1 
    for m in range(start + 1, width - 1):
        if(black[m] if arg else white[m]) > (0.98 * black_max if arg else 0.98 * white_max):
            end = m
            break
    return end

if __name__ == 'main':
    img = cv2.imread(r'D:\pyrhon_test\5.License Plate Localization and Recognition\License Plate1.bmp', cv2.IMREAD_COLOR)     #讀取影像
    #前置處理影像
    rect, afterimg = find_license(img)
    #框出車牌號碼
    cv2.rectangle(afterimg, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)
    cv2.imshow('afterimg', afterimg)
    #分割車牌與背景
    cutimg = cut_license(afterimg, rect)
    cv2.imshow('cutimg', cutimg)
    #二值化
    thresh = deal_license(cutimg)
    cv2.imshow('thresh', thresh)
    cv2.waitKey(0)
    #分割字元
    '''判斷底色和字色'''
    #紀錄黑白像素總和
    white = []
    black = []
    height = thresh.shape[0]
    width = thresh.shape[1]
    white_max = 0
    black_max = 0
    #計算每列的黑白像素總和
    for i in range(width):
        line_white = 0
        line_black = 0
        for j in range(height):
            if thresh[j][i] == 255:
                line_white += 1
            if thresh[j][i] == 0:
                line_black += 1
        white_max = max(white_max, line_white)
        black_max = max(black_max, line_black)
        white.append(line_white)
        black.append(line_black)
        print('white', white)
        print('black', black)
    #arg為True表示黑底白字，False為白底黑字
    arg = True
    if black_max < white_max:
        arg = False
    n = 1
    start = 1
    end = 2
    s_width = 28
    s_height = 28
    while n < width - 2:
        n + 1
        #判斷是否白底黑字還是黑底白字0.05參數，對應上面0.95可做調整
        if(white[n] if arg else black[n]) > (0.02 * white_max if arg else 0.02 * black_max):
            start = n
            end = find_end(start, arg, black, white, width, black_max, white_max)
            n = end
            if end - start > 5 :
                cj = thresh[1:height, start:end]
                print('result/%s.bmp' % (n))
                #保存分割的影像 by cayden
                infile = 'result/%s.bmp' % (n)
                io.imsave(infile, cj)
                cv2.imshow('cutlicense', cj)
                cv2.waitKey(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

