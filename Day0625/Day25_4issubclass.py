class Base(object):
    pass
class Foo(Base):
    pass
class Bar(Foo):
    pass

print(issubclass(Foo,Base))  #检查第一个参数是否是第二个参数的子类
print(issubclass(Bar,Base))  #检查第一个参数是否是第二个参数的子类

##  type  isinstance() 对象,类  是否是类的实例化 

