class Base():
    def f1(self):
        super().f1()
        print('Base.f1')

class Bar():
    def f1(self):
        print('Bar.f1')

class Foo(Base,Bar):
    pass

obj = Foo()  #Foo -> Base -> Bar
obj.f1()