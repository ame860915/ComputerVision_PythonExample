import numpy as np
from scipy.sparse import csr_matrix

indptr = np.array([0,2,3,5,6])      #每行包含幾個元素
indices = np.array([0,2,2,0,1,2])   #元素所在行數
data = np.array([1,2,3,4,5,6])      #要壓縮的數據
a = csr_matrix((data,indices,indptr),shape=(4,3)).toarray()
print('稀疏矩陣a為:\n',a)

b = csr_matrix(a)
print('稀疏矩陣b為:\n',b)

####
#shape = (row,col) 先列再行
####
#indptr代表有多少列，並記錄每列有多少個數字。
#ex:2-0=2 第一列有兩個數字，3-2=1 第二列有一個數字，5-3=2 第三列有兩個數字，6-5=1 第四列有一個數字。
####
#indices代表相對應的data在第幾行
#ex:indices[0]=0 =>數據1在第0行，indices[1]=2 =>數據2在第2行，indices[2]=2 =>數據3在第2行，
#   indices[3]=0 =>數據4在第0行，indices[4]=1 =>數據5在第1行，indices[5]=2 =>數據6在第2行
####
#至於如何得知稀疏矩陣，在於數據依序排列，依據indptr知道第一列有幾個非0數值存在，indices可得知非0數值存在第幾行
