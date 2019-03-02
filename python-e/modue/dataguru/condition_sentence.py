# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 16:05:26 2016
条件控制语句
@author: pujie
"""
'''1:
if condition_1:
    执行语句
elseif conditon_2:
    执行语句2
elseif condition3:
    执行语句3
eles:
    默认执行语句(pthon基础语言包不支持switch)
'''
flag = False
name = 'python'
if name == 'python':
    flag = True
    print('welcome boss.')
else:
    print(name)
    
'''2:
 while condition:
     执行语句
else:
    执行语句 (正常执行完while后执行,用break不会执行else)
'''   
count=1
while count < 10:
    print('The count is',count)
    count +=1
else:
    print('Good bye.')

'''3:
for item in sequence:
    statements(s)
'''
for letter in 'Python':
    print('current character is',letter)
    
fruits = ['banana','apple','mango']
for fruit in fruits:
    print('当前水果:',fruit)
print('Good bye')
#序列索引迭代
for index in range(len(fruits)):
    print('当前水果:',fruits[index])
print('Good bye.')
#for ... else (求质数)
for num in range(10,20):   #迭代10 到20 之间的数字
    for i in range(2,num): #根据因子迭代
        if num%i == 0:     #能整除则i为第一个因子
            j=num/i        #确定第二个因子
            print('%d = %d * %d' % (num,i,j))
            break          #跳出循环
    else:
        print(num,'是一个质数')

#自定义函数
sum=lambda arg1,arg2:arg1+arg2
print('求和:',sum(1,2))