#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'rtb 服务的模拟client'


print('1','请输入一个数字')

index = int(input())
if index > 0:
    print("index 的绝对值：",index)
else:
    print("index 的绝对值：",-index)

'小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：'
#•低于18.5：过轻
#•18.5-25：正常
#•25-28：过重
#•28-32：肥胖
#•高于32：严重肥胖3

height=1.7
weight=100
bmi=weight/(height * height)
if bmi < 18.5:
    print('您的bmi为%.2f：过轻' %bmi)
elif bmi < 25:
    print('您的bmi为%.2f：正常' %bmi)
elif bmi < 28:
    print('您的bmi为%.2f：过重' %bmi)
elif bmi < 32:
    print('您的bmi为%.2f：肥胖' %bmi)
else:
    print('您的bmi为%.2f：严重肥胖' %bmi)
#常用内置函数
print('利用abs求-10的绝对值：',abs(-10))
print('max求2,4,10,100,2,3的最大值：',max(2,4,10,100,2,3))
