class Base:
    def f2(self):
        print('来Base的f2')
#继承自Base
class Foo(Base):
    def f1(self):
        print('来自Foo的f1')

obj = Foo()
obj.f1()
obj.f2()
#总结: self是哪个类的对象,那么就从该类开始找(自己没有就找父类)