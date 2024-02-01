import cv2
import numpy as np

def zmMinFilterGray(src, r=7):
    '''最小值濾波，r是濾波器半徑'''
    return cv2.erode(src, np.ones((2 * r + 1, 2 * r + 1)))

def guidedfilter(I, p, r, eps):
    height, width = I.shape
    m_I = cv2.boxFilter(I, -1, (r, r))
    m_p = cv2.boxFilter(p, -1, (r, r))
    m_Ip = cv2.boxFilter(I *  p, -1, (r, r))

    cov_Ip = m_Ip - m_I * m_p
    m_II = cv2.boxFilter(I * I, -1, (r, r))
    var_I = m_II - m_I * m_I

    a = cov_Ip / (var_I + eps)
    b= m_p - a * m_I
    m_a = cv2.boxFilter(a, -1, (r, r))
    m_b = cv2.boxFilter(b, -1, (r, r))

    return m_a * I + m_b

def Defog(m ,r, eps, w, maxVl):                 #輸入rgb影像，數值範圍[0, 1]
    '''計算大氣隱藏影像V1和光源值A, V1 = 1 -t / A'''
    Vl = np.min(m, axis=2)                           #得到暗通道影像
    Dark_Channel = zmMinFilterGray(Vl, 7)
    cv2.imshow('wu_Dark', Dark_Channel)         #查看暗通道
    cv2.waitKey(0)

    cv2.destroyAllWindows()
    Vl = guidedfilter(Vl, Dark_Channel, r, eps)  #使用啟動濾波最佳化
    bins = 2000
    ht = np.histogram(Vl, bins)                  #計算大氣光源A
    d = np.cumsum(ht[0]) / float(Vl.size)
    for lmax in range(bins - 1, 0, -1):
        if d[lmax] <= 0.999:
            break
    A = np.mean(m, 2)[Vl >= ht[1][lmax]].max()
    Vl = np.minimum(Vl * w, maxVl)              #對值範圍進行限制
    return Vl, A

def deHaze(m, r=81, eps=0.001, w=0.95, maxVl= 0.80, bGamma=False):
    Y = np.zeros(m.shape)
    Mask_img, A = Defog(m, r, eps, w, maxVl)    #得到隱藏影像和大氣光源
    for k in range(3):
        Y[:, :, k] = (m[:, :, k] - Mask_img) / (1 - Mask_img / A)   #顏色校正
    Y = np.clip(Y, 0 , 1)
    if bGamma:
        Y = Y ** (np.log(0.5)) / np.log(Y.mean())   #gamma校正，預設不進行該操作
    return Y

if __name__ == '__main__':
    m = deHaze(cv2.imread(r"D:\pyrhon_test\2.Image Dehazing Technology\image.bmp") / 255.0) * 255
    cv2.imwrite("D:\pyrhon_test\2.Image Dehazing Technology\image2.bmp", m)

