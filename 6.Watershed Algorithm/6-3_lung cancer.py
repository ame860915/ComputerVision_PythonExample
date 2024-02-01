import cv2 as cv 
import numpy as np 

def watershed_demo(img):
    print(img.shape)
    #去雜訊
    blurred = cv .pyrMeanShiftFiltering(img, 10, 100)
    #灰階/二值影像
    gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)
    ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('(b)thresh', thresh)
    cv.imwrite(r'D:\pyrhon_test\6.Watershed Algorithm\image\(b)thresh.bmp', thresh)
    #有很多的黑點，所以我們去黑點雜訊
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    opening = cv.morphologyEx(thresh,cv.MORPH_OPEN, kernel, iterations=2)
    cv.imshow('(c)opening', opening)
    cv.imwrite(r'D:\pyrhon_test\6.Watershed Algorithm\image\(c)opening.bmp', opening)
    sure_bg = cv.dilate(opening, kernel, iterations=3)
    cv.imshow('(d)mor-opt', sure_bg)
    cv.imwrite(r'D:\pyrhon_test\6.Watershed Algorithm\image\(d)mor-opt.bmp', sure_bg)
    #距離變換
    dist = cv.distanceTransform(opening, cv.DIST_L2, 3)
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    cv.imshow('(e)distance-t', dist_output * 50)
    cv.imwrite(r'D:\pyrhon_test\6.Watershed Algorithm\image\(e)distance-t.bmp', dist_output * 50)
    ret, surface = cv.threshold(dist, dist.max() * 0.6, 255, cv.THRESH_BINARY)
    cv.imshow('(f)surface', surface)
    cv.imwrite(r'D:\pyrhon_test\6.Watershed Algorithm\image\(f)surface.bmp', surface)

    #發現未知的區域
    surface_fg = np.uint8(surface)
    cv.imshow('(g)surface_bin', surface_fg)
    cv.imwrite(r'D:\pyrhon_test\6.Watershed Algorithm\image\(g)surface_bin.bmp', surface_fg)
    unknow = cv.subtract(sure_bg, surface_fg)

    #標記標籤
    ret, markers = cv.connectedComponents(surface_fg)
    #增加一個標籤到所有標籤，這樣確保背景不是0，而是1
    markers = markers + 1
    #令未知的為零
    markers[unknow == 255] = 0
    markers = cv.watershed(img, markers)
    img[unknow == -1] = [255, 0, 0]
    cv.imshow('(h)result', img)
    cv.imwrite(r'D:\pyrhon_test\6.Watershed Algorithm\image\(h)result.bmp', img)

img = cv.imread(r'D:\pyrhon_test\6.Watershed Algorithm\lung cancer.bmp')
#cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
cv.imshow('(a)img', img)
cv.imwrite(r'D:\pyrhon_test\6.Watershed Algorithm\image\(a)img.bmp', img)
watershed_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()