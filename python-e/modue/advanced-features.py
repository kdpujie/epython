import os
#高级特性
#1,切片
L = list(range(10))
print('1,切片：L[0:3]表示从索引0开始取值，直到索引3为止，但不包括3。如果第一个索引是0，还可以省略成 L[:3]')
print(' L全值：')
print('    ',L)
print(' L[:3]:取前三个元素')
print('    ',L[:3])
print(' L[-2:]:取倒数两个元素')
print('   ',L[-2:])
print(' L[::2]:每两个取一个')
print('  ',L[::2])
print(' L[:]:复制一个list')
print('  ',L[:])
#2,迭代
d = {'a':1,'b':2,'c':3}
print('  迭代dict的key-value对：')
for key,value in d.items():
    print(key,value)
print('  迭代dict的key：')
for key in d:
    print(key)
print('  迭代dict的value:')
for value in d.values():
    print(value)
print('利用Python内置的enumerate函数实现list的下标循环：')
for i,value in enumerate(['a','b','c','d','e']):
    print(i,value)

print('字符串迭代：')
for ch in 'abc':
    print(ch)
#3,列表生成式
print('使用循环生成列表[1*1,2*2,...,10*10]')
L = [ x*x for x in range(1,11)]
print('    ',L)
print('利用if筛选出偶数的平方：')
L = [x*x for x in range(1,11) if x%2 ==0]
print('    ',L)
print('使用两层循环，生成全排列')
L = [ m+n for m in 'ABC' for n in '123']
print('    ',L)
print('列出当前目录下的所有目录和文件名：')
L = [d for d in os.listdir('.')]
print('   ',L)
print('循环操作两个变量：')
d = {'a':'97','b':'98','c':'99'}
L = [ k+'='+v for k,v in d.items()]
print('    ',L)
print('把list中所有的字符串变成小写：')
L = ['Hello',8,'World',18,'IBM','Apple']
L1 = [s.lower() for s in L if isinstance(s,str)]
print('    ',L1)

#4,生成器(generator)
print('[列表生成式],定义[1*1,2*2,...,10*10]的生成器，并for循环迭代求和：')
g = (x*x for x in range(1,11))
sums = 0;
for n in g:
    sums = sums + n
print(sums)
print('------------斐波拉契数列---------------')
def bif(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a + b
        n = n + 1
    return b;
print(' 遍历：')
for n in bif(10):
    print(n)
b = bif(10)
while True:
    try:
        x = next(b)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
print('------------杨辉三角----------------------------')
def yanghui(max):
    L = [1]
    n = 0
    while n < max:
        yield L
        a,b = L,L
        L = [m+n for m,n in zip([0]+L,L+[0])]
        n = n+1
for n in yanghui(10):
    print(n)















    
