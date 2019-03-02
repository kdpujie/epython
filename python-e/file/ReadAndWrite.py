'''
Created on 2015年11月13日

@author: pujie
'''
import logging

def baseReadFile():
    try:
        f=open('E:\py-workspace\practice-file\hello.txt','r',encoding='utf-8',errors='ignore')
        #print(f.read()) #一次读取文件全部内容
        str = f.readline() #读取整行
        while(str):
            print(str)
            str=f.readline()
    except BaseException as e:
        logging.exception(e)
    finally:
        f.close()
#利用with语句自动调用close函数，使代码简介。
def simpleReadFile():
    with open('E:\py-workspace\practice-file\hello.txt','r') as f:
        for line in f.readlines():
            print(line)
#写文件
def baseWriteFile():
    try:
        f=open('E:\py-workspace\practice-file\hello.txt','a',encoding='gbk')
        f.write('\n')
        f.write('你')
    finally:
        f.close()    
def main():
    baseReadFile()
    
main()    