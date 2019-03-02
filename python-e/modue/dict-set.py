#dict联系
d = {'张飞':95,'吕布':99,'赵云':98,'关羽':98}
print('张飞的武力值：',d['张飞'])
print('吕布的武力值：',d.get('吕布'))
print('刘备的武力值：',d.get('刘备'))
d['刘备']=82
print('刘备的武力值：',d.get('刘备'))
d.pop('刘备')
print('刘备的武力值：',d.get('刘备'))
#set 无序不重复
s1 = set([1,1,2,3,4,4])
s2 = set([1,4,5,10,11,20])
print(s1)
s1.add(5)
s1.remove(4)
print(s1)
print('s1和s2交集：',s1 & s2)
print('s1和s2并集',s1 | s2)
l = [11,22,33]
s1.add(l)
print(s1)
