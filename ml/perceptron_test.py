#encoding=utf-8
'''
感知机算法的原始形式简单实现
Created on 2019年3月2日
@author: jie.pu
'''

import xlrd

def read_data(file):
    book = xlrd.open_workbook(file)
