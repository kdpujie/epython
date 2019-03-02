'''
Created on 2015年11月20日

@author: pujie
'''
import json

class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

def use_json():
    d = dict(name='Bob',age=20,score=88)
    print('把dict转换成json串\n\t',json.dumps(d))
    json_str = '{"score": 88, "age": 20, "name": "Bob"}'
    print('把json串转化为dict对象\n\t',json.loads(json_str))
    
    s = Student('Bob',20,88)
    print(json.dumps(s))
    
    
use_json()