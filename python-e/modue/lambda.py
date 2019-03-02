from functools import reduce
#lambda表达式
f=lambda x,y,z:x+y+z
print(f(1,2,3))

n=5
f1=reduce(lambda x,y:x*y,range(1,n+1))
print(f1)

def action(x):
    return lambda y:x+y
ff=action(2)
print(ff(22))
