class Foo(object):
    def __init__(self, a1, a2):
        print('__init__ successful!!!')
        self.a1 = a1
        self.a2 = a2

    def __call__(self, *args, **kwargs):
        print(111, args, kwargs)

    def __getitem__(self, item):
        print('__getitem__', item)

    def __setitem__(self, key, value):
        print(key, value, 10101010)

    def __delitem__(self, key):
        print(key, 'Delete %s successful' % key)


# 类名()  自动执行__init__
obj = Foo(1, 2)

# 对象() 自动执行 __call__
obj(2, 3, 4, k1=123, k2=234, k3=345)

v1 = {'k1': 'kk1', 'k2': 'kk2', 'k3': 'kk3'}
v2 = [12, 23, 21, 33]
print(v1, type(v1))
print(v2, type(v2))
print(v1['k1'])
print(v2[3])

# 对象[]  自动执行 __getitem__
obj['Jiandandian']

# 对象[] = xxx   自动执行 __setitem__
obj['k1'] = 'Fuzadian'

# del 对象[]  自动执行 __delitem__
del obj['uiotre']
