#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'引入模块，使用其提供的功能'

__author__ = 'jie.pu'

from collections import namedtuple,deque,defaultdict, OrderedDict


def use_namedtuple():
    Point=namedtuple('Point',['x','y'])
    p = Point(1,2)
    print('x坐标：',p.x,'\ny坐标：',p.y)


#deque双向列表
def use_deque():
    q=deque(['a','b','c','d'])
    print(q)
    q.append('x')
    q.appendleft('y')
    print(q)


#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
def use_defaultdict():
    d = defaultdict(lambda:'')
    d['a']=97
    d['b']=98
    d['c']=99
    print(d['d'])


#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#OrderedDict的Key会按照插入的顺序排列
def use_orderedDict():
    d = OrderedDict([('a',97),('b',98),('c',99)])
    print(d)


if __name__ == '__main__':
    use_namedtuple()
    use_deque()
    use_defaultdict()
    use_orderedDict()