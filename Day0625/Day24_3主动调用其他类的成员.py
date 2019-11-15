#############################方法一######################
class Base():
    def f1(self):
        print('5个功能')


class Foo():
    # class Foo(object):  这样写也可以调用到Base()里面的函数,跟自动调用以及这节涉及的东西没有关系
    def f1(self):
        print('3个功能')
        # self不会自动传参
        Base.f1(self)


# obj = Foo()
# obj.f1()


# 主动调用其他类的成员
###########################方法二##########################
class Base():
    def f1(self):
        print('5个功能')


class Foo(Base):
    # class Foo(object):  这样写也可以调用到Base()里面的函数,跟自动调用以及这节涉及的东西没有关系
    def f2(self):
        print('Super Testing....')
        # super  按照类的继承顺序找下一个
        super().f1()


# obj = Foo()
# obj.f2()

######  方式二:按照类的继承顺序,找下一个
class First(object):
    def f1(self):
        super().f1()   #print('Second function')
        print('First function')

class Second():
    def f1(self):
        # super().f1()
        print('Second function')

class Info(First, Second):
    pass

# obj = Info()
# obj.f1()

class Four(First,Second):
    def bb(self):
        super().f1()
        # 5个功能
        # Second function
        # First function
        print('111')
obb = Four()
obb.bb()