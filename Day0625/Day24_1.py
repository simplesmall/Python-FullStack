class Foo(object):
    @classmethod
    def f3(cls):
        print(cls)

obj = Foo()
obj.f3()