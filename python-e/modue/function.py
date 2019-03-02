#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'函数定义'

import math

'1,普通函数：求二元一次方程的解'
print('1,普通函数，求解二元一次方程的解')
def quad(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('bad type error a')
    if not isinstance(b,(int,float)):
        raise TypeError('bad type error b')
    if not isinstance(c,(int,float)):
        raise TypeError('bad type error c')
    flag = b*b - 4*a*c
    if a == 0:
        x = -c/b
        return float('%.2f'%x)
    elif flag>0:
        x1 = (-b + math.sqrt(flag))/(2*a)
        x2 = (-b - math.sqrt(flag))/(2*a)
        return float('%.2f'%x1),float('%.2f'%x2)
    elif flag == 0:
        x = -b / (2 * a)
        return float('%.2f'%x)


print('  x1,x2的解：',quad(2,3,1))
'2,带默认参数的函数：求解n的m次方，默认为2次方。'
print('2,带默认参数的函数：求解n的m次方，默认为平方')
def power(n,m=2):
    s = 1
    while m>0:
        m = m-1
        s = s * n
    return s
print('  8的平方=',power(8))
print('  8的立方=',power(8,3))


'3,可变参数,在函数内部相当于接收到一个tuple。计算：a2 + b2 + c2 + ……'
print('3,可变参数，计算：a2 + b2 + c2 + ……')
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print('  1平方+2平方+3平方+4平方：',calc(1,2,3,4))
nums = [3,5,7,9]
print('  3平方+5平方+7平方+9平方：',calc(*nums))


'4,关键字参数。'
print('4,关键字参数')
def person(name,age,**kw):
    kw['性别']='男'
    print('  name:',name,'age:',age,'other:',kw)
person('蒲  杰',28)
person('李晓龙',28,city='beijing',job='Enginneer')
extra = {'city':'shenzheng','job':'enginneer'}
person('刘海峰',29,**extra)


'5,命名关键字参数'
print('5,命名关键字参数')
def person(name,age,*,city,job):
    print(name,age,city,job)
person('  赵云',56,city='蜀国',job='武将')


'6,参数组合，参数定义顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数'
print('6,参数顺序：必选参数、默认参数、可变参数/命名关键字参数和关键字参数')


def f1(a,b,c=0,*args,**kw):
    print('   a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)


def f2(a,b,c=0,*,d,**kw):
    print('   a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)


print('  f(1,2):')
f1(1,2)
print('  f(1,2,3):')
f1(1,2,3)
print('  f(1,2,3,a,b):')
f1(1,2,3,'a','b')
print('  f(1,2,3,a,b,x=99):')
f1(1,2,3,'a','b',x=99)
print('  f(1,2,d=99,ext=None):')
f2(1,2,d=99,ext=None)
print('通过tuple和dict调用以上函数：')
args = (1,2,3,4)
kw = {'d':99,'x':'#'}
f1(*args,**kw)

























