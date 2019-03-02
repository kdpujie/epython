'''
Created on 2015年12月11日

@author: pujie
'''
import hashlib

#MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
def use_md5():
    md5 = hashlib.md5()
    md5.update('hello world'.encode(encoding='utf_8', errors='strict'))
    print(md5.hexdigest())
    
#SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
def use_sha1():
    sha1 = hashlib.sha1()
    sha1.update('how to use sha1 in'.encode(encoding='utf_8', errors='strict'))
    sha1.update('python hashlib'.encode('utf-8','strict'))
    print(sha1.hexdigest())

if __name__ == '__main__':
    use_md5()
    use_sha1()