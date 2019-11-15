class Foo(object):
    def __init__(self):
        pass

    @property
    def start(self):
        return 1

    def end(self):
        return 10


obj = Foo()
#这样的情况下调用不用加括号(),而且在定义的时候括号里面不能加参数
print(obj.start)
#这样的情况下调用需要加括号(),而且在定义的时候括号里面能加参数
print(obj.end())
#无需传参且有返回值的时候  调用: 对象.方法