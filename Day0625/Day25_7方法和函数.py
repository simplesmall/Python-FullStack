def func():
    pass


print(func)


class Foo(object):
    def detail(self):
        pass

    @staticmethod
    def xxx():
        pass


obj = Foo()
print(obj.detail)
print(Foo.xxx)

###   用科学的方法判断是函数还是方法
from types import MethodType, FunctionType


def check(arg):
    if isinstance(arg, MethodType):
        print('arg是一个方法')
    elif isinstance(arg, FunctionType):
        print('arg是一个函数')
    else:
        print('arg既不是函数也不是方法')


check(obj.detail)
check(func)

#######    一般而言如果是方法的话 self 不用自己传
class test(object):
    def f1(self):
        pass
obj = test()
#  以下调用方式最后结果是一样的
print(obj.f1)    #此处调用是  方法
print(test.f1)   #此处调用是  函数 但是以这种方式调用的话必须自己手动传参

# obj.f1()
# test.f1(obj)

