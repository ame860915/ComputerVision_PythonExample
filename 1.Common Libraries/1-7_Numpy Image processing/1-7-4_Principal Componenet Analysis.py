from PIL import Image
from numpy import *
def pca(X):
    '''主成份分析
    輸入:矩陣X，其中該矩陣中儲存訓練資料，每一行為一筆訓練資料
    返回:投影矩陣(按照維度的重要性排序)、方差和平均值
    '''
    #獲得維度
    num_data, dim = X.shape
    #資料中心化
    mean_X = X.mean(axis = 0)
    X = X - mean_X

    if dim > num_data:
        #PCA - 使用繁致技巧
        M = dot(X, X.T)     #協方差矩陣
        e, EV = linalg.eigh(M)  #特徵值和特徵向量
        tmp = dot(X.T, EV).T    #**這就是緊致技巧**
        V = temp[::-1]          #由於最後的特徵向量是我們所需要的，所以需要將其逆轉
        S = sqrt(e)[::-1]       #由於特徵值是按照遞增順序排列的，所以需要將其逆轉
        for i in range(V.shape[1]): 
            V[:, i] /= S
    else:
        #PCA - 使用SVD方法
        U, S, V = linalg.svd(X)
        V = V[:num_data]        #僅返回前num_data維的資料才合理
    
    #返回投影矩陣、方差和平均值
    return V, S, mean_X