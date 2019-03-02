from functools import reduce
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}.get(s)
def merge(x,y):
    return x * 10 + y
def str2int(s):
    return reduce(merge,map(char2num,s))
print('利用map/reduce实现str2int功能:',str2int('1223'))
print('------------map 规范英文名格式 -----------------------')
#可利用str.capitalize()函数把首字母格式化为大写。
def normalize(name):
    temp = ''
    temp = temp + name[0].upper()
    for i in range(1,len(name)):
        temp = temp + name[i].lower()
    return temp
L = ['adam', 'LISA', 'barT']
print('',list(map(normalize,L)))
print('-------------利用reduce函数，求给定序列元素的乘积-------------')
def mutil(x,y):
    return x * y
def prod(L):
    return reduce(mutil,L)
L1 = [1,2,3]
print('',prod(L1))
print('------------filter---------------------------')
print('过滤序列中的空字符')
def not_empty(s):
    return s and s.strip()
L2 = ['A',' B','c ',' d ','','  ']
print('过滤前：',L2)
print('过滤后：',list(filter(not_empty,L2)))
#构造一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0
#生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() #初始序列,大于2的偶数肯定不是素数
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it) #构造新序列
for n in primes():
    if n < 10:
        print(n)
    else:
        break
print('-------------------sorted-------------------------------')
def _first(t):
    return t[0]
print(_first(('a','b')))
