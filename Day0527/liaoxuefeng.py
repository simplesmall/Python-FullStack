import math

print(int('123'))
print(int(12.34))
a = abs
print(a(-123))

def choose(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if(x>0):
        print('You are so lucky')
        return x
    elif(x<-2):
        print('Not so lucky')
        return -x
    else:
        pass
print(choose(1))

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

r = move(100, 100, 60, math.pi / 6)
print (r)

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
r = add_end()
print(r)
s=add_end([1, 2, 3])
print(s)

# 可变参数的函数定义方法
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(12,2,3))
# 对于已经是list或者tuple的可以采用此种方法来实现运算
nums = [1,2,3,4]
print(calc(*nums))

# 除了传入必须的参数以外,还可以灵活传入任意个数的关键字参数,其中是以dict方式存储
def person(name,age,**kw):
    print('name',name,'age',age,'other',kw)

print(person('Bill',21,city='yunnan',sex='male'))

# 如上,如果已有的dict如何运用进关键字参数中
kw = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, city=kw['city'], job=kw['job']))

# 或者以这种方式来进行运算和添加
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw)

def func(a, b, c=0, *args, **kw):
    print ('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
print(func(1,2,3,'a','b',x=123))
# 另一种通过一个list 和dict调用该函数的方法
args = (1, 2, 3, 4)
kw = {'x': 99}
print(func(*args, **kw))
"""
对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
"""
