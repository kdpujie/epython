'''
Created on 2015年11月13日

@author: pujie
'''
from _io import StringIO, BytesIO


def useStrIO():
    s = StringIO()
    s.write('hello,world!')
    s.write('\n')
    s.write('hello,BeiJing!')
    #print(s.getvalue()) #获取所有信息
    printStrIO(s)


#BytesIO实现了在内存中读写bytes
def useByteIO():
    b = BytesIO()
    b.write('中文'.encode(encoding='utf_8'))
    printStrIO(b)
    #print(b.getvalue())


'逐行获取IO里的内容'
def printStrIO(strIO):
    strIO.seek(0)  #把stream position移动到原始位置
    while True:
        s = strIO.readline()
        if str(s)=='' or str(s)=='b\'\'':
            break
        print(s)
    
useByteIO()