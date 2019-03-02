'''
Created on 2015年11月16日
操作文件和目录
@author: pujie
'''
import os
from _datetime import datetime
def dir_l(path):
    for f in os.listdir(path):
        abspath=os.path.join(path,f) #定位文件 绝对路径
        fsize = os.path.getsize(abspath)
        mtime = datetime.fromtimestamp(os.path.getmtime(abspath)).strftime('%Y-%m-%d %H:%M:%S') #时间格式化
        flag = '/' if os.path.isdir(abspath) else ''
        print("%10d %s %s%s" % (fsize,mtime,f,flag))  #格式化输出
#找文件名包含指定字符串的文件（递归实现）。
def search_file0(path,str):   
    for f in os.listdir(path):
        abspath=os.path.join(path,f) #定位文件 绝对路径
        if(os.path.isfile(abspath) and f.find(str)>-1):
            print(abspath)
        elif(os.path.isdir(abspath)):
            sub_path = os.path.join(path,abspath)
            search_file0(sub_path,str)
#找文件名包含指定字符串的文件（非递归实现）。
def search_file1(dir,str):
    rs = []
    flds = [dir]
    for d in flds:
        for f in os.listdir(d):
            abspath=os.path.join(d,f) #定位文件 绝对路径
            if(os.path.isdir(abspath)):
                flds.append(abspath)
            elif(os.path.isfile(abspath) and f.find(str)>-1):
                rs.append(f)
    print('%s files founded in searching \'%s\' at \'%s\':' % (len(rs),str,dir))
    for r in rs:
        print('%s'%r)
    return rs

def main():
    path = os.path.abspath('E:\\py-workspace\\modue')
    search_file1(path,'o')
    
main()