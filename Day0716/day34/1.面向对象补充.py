'''
面向对象的方法
'''
"""
class Foo(object):
    def  __init__(self):
        self.info = {}

    def __setitem__(self, key, value):
        # print(key, value)
        self.info[key] = value

    def __getitem__(self, item):
        # return 123
        return self.info.get(item)

obj = Foo()
obj['x'] = 123
print(obj['x'])
"""


class Foo(object):
    def __init__(self):
        self.name = 'alex'

    def __setattr__(self, key, value):
        print(key, value)

    def __getattr__(self, item):
        return 123


# obj = Foo()  #调用__init__ 函数
# obj.y = 123
# print(obj.y)

class Bar(object):
    def __init__(self):
        # self.name = 'bilibili'  #默认自己类中执行   __setattr__
        # self.info= {}
        object.__setattr__(self,'info',{})  #给对象中设置  name = 'alex'

    def __setattr__(self, key, value):
        # object.__setattr__(self,key,value)  #给对象中设置  name = 'alex'
        self.info[key] = value
    def __getattr__(self, item):
        return self.info[item]
obj = Bar()
# print(obj.name)
# print(obj.info)
obj.name = 'alex'
print(obj.info['name'])

obj.x = 133
