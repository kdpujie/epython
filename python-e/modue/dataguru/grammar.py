# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 20:01:53 2016

@author: pujie
"""

print "hello world"
print ("hello,python!")

#行和缩进
if True:
    print "现在的条件成立"
    print "True"
else:
    print "False"
    
#多行语句
item_one=1
item_two=2
item_three=3
total = item_one + \
        item_two + \
        item_three
print total

'''
多行注释
'''
word = 'word'
sentence = "this is a sentence."
paragraph = """这是一个段落.
包含了多个段落"""
print paragraph
import sys;
#空行
'''
raw_input("\n\nPress the enter key to exit.")

x = 'foo';
sys.stdout.write(x+'\n')
'''
#帮助
help (sys.stdout.write)

#变量赋值
counter= 100   #整型变量
miles = 1000.0 #浮点型
name = "John"  #字符型
a=b=c=1
a,b,c=1,2,"hello"

print counter
print miles
print name
print a,b,c

#字符串
#s="abcd....z"
s = 'iLovePython'
print s[1:-1]

#列表
list=['abcd',789,2.23,'john',70.2]
tinylist=[123,'john']

print "输出列表第一个元素:",list[0] #输出列表的第一个元素

#元字典
dict={}
dict['one']="This is one"
dict[2]="this two"

tinydict = {'name':'john','code':6379,'dept':'sales'}

print dict
print tinydict


