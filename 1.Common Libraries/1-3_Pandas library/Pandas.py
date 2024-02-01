import pandas as pd
from pandas import Series,DataFrame

print('用一維陣列生成Series')
x = Series([1,2,3,5])
print(x)

print(x.values)     #[1 2 3 5]
#預設標籤為 0 到 3 的序號
print(x.index)      #RangeIndex(start=0, stop=4, step=1)

print('指定Series 的 index')    #可將index了解為行索引
x = Series([1,2,3,5], index = ['a','b','d','c'])
print(x)
print(x.index)  #Index([u'a', u'b', u'd', u'c'], dtype='object')
print('--------')
print(x['a'])
x['d'] = 6  #透過行索引來取得設定值
print(x[['c','a','d']])   #類似於numpy的花式索引