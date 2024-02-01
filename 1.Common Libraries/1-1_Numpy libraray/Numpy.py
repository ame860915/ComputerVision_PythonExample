import numpy;

print("使用串列生成一維陣列")
data = [1,2,3,4,5,6]
x = numpy.array(data)
print(x)                        #列印陣列
print(x.dtype)                  #列印陣列元素的類型

print('使用串列生成二維陣列')
data = [[1,2],[3,4],[5,6]]
x = numpy.array(data)
print(x)                        #列印陣列
print('陣列的維度:', x.ndim)    #列印陣列的維度
print('陣列的維度長度:',x.shape) #列印陣列各個維度的長度.shape是一個元組