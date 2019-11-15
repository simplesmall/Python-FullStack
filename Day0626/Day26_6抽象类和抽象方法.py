from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta): #抽象类
    def f1(self):
        print(123)

    @abstractmethod  #抽象方法
    def f2(self):
        pass

class Foo(Base):
    def f2(self):  #抽象方法必须实现
        print(666)

obj = Foo()
obj.f1()
obj.f2()