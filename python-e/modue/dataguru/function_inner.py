# -*- coding: utf-8 -*-
'''
常用内置函数
'''
#向量相加-(Python实现)
def pythonsum(n):
    a = range(n)
    b = range(n)
    c = []
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    return c

#向量相加-(NumPy实现)
import numpy
import numpy as np

def numpysum(n):
    a = numpy.arange(n) ** 2
    b = numpy.arange(n) ** 3
    c = a + b
    return c

#效率比较(pyton和numpy)
from datetime import datetime

size = 1000

start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start
print "The last 2 elements of the sum", c[-2:]
print "PythonSum elapsed time in microseconds", delta.microseconds

start = datetime.now()
c = numpysum(size)
delta = datetime.now() - start
print "The last 2 elements of the sum", c[-2:]
print "NumPySum elapsed time in microseconds", delta.microseconds

#numpy数组
a = numpy.arange(5)
a.dtype   

a
a.shape   #查看数据维度
#创建多维数组
m = np.array([np.arange(2), np.arange(2)])

print m

print m.shape

print m.dtype

np.arange(15)

print '大小为10的一维数组',np.zeros(10)
print '3 x 6的二维数组',np.zeros((3, 6))
print '2x3x2的三维数组'
print np.zeros((2, 3, 2))

#选取数组元素
a = np.array([[1,2],[3,4]])

print "In: a"
print a

print "In: a[0,0]"
print a[0,0]

print "In: a[0,1]"
print a[0,1]

print "In: a[1,0]"
print a[1,0]

print "In: a[1,1]"
print a[1,1]

#numpy数据类型
print 'numpy数据类型:'
print "In: float64(42)"
print np.float64(42)

print "In: int8(42.0)"
print np.int8(42.0)

print "In: bool(42)"
print np.bool(42)

print np.bool(0)

print "In: bool(42.0)"
print np.bool(42.0)

print "In: float(True)"
print np.float(True)
print np.float(False)

print "In: arange(7, dtype=uint16)"
print np.arange(7, dtype=np.uint16)

# 数据类型转换
print '--数据类型转换:'
arr = np.array([1, 2, 3, 4, 5])
arr.dtype
float_arr = arr.astype(np.float64)
float_arr.dtype

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
arr
arr.astype(np.int32)

numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_strings.astype(float)
print '--Good bye.'
#数据类型对象
print '--数据类型对象:'
a = np.array([[1,2],[3,4]])

print a.dtype.byteorder

print a.dtype.itemsize

#字符编码
print '--dtype 类型代码'
print np.arange(7, dtype='f')
print np.arange(7, dtype='D') #复数

print np.dtype(float)

print np.dtype('f') #单精度

print np.dtype('d') #双精度


print np.dtype('f8') #双精度

print np.dtype('Float64') #双精度

#dtype类的属性
print '--dtype类的属性:'
t = np.dtype('Float64')

print 'dtype.char=',t.char

print 'dtype.type=',t.type

print 'dtype.str:',t.str

#创建自定义数据类型
print '--创建自定义的数据类型: 名称(name),数量(numitems),价格(price):'
t = np.dtype([('name', np.str_, 40), ('numitems', np.int32), ('price', np.float32)])
print t

print t['name']

itemz = np.array([('Meaning of life DVD', 42, 3.14), ('Butter', 13, 2.72)], dtype=t)

print itemz[1]

