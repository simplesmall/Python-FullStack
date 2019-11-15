class Foo:
    # 类变量
    country = '中国'

    def __init__(self, name):
        self.name = name
        self.__age = 23

    def func(self):
        print(self.name, self.__age)


obj = Foo('Jianxiao')
# 默认的自带一个参数self,在此处是每个指定的类的类名,比如此处就是obj
obj.func()
# 根据使用的作用看见通过类或对象来 . 使用
print(obj.country)


# 方法分为: 实例方法  静态 方法  类方法

class Bar:
    def __init__(self, name):
        self.name = name

    def func(self):
        print(self.name)

    @staticmethod
    def display():
        print('666')


ojbk = Bar('史泰龙')
ojbk.display()
# 静态方法虽然两种调用方法都可以,但是一般推荐类调用
Bar.display()


# 编写时:
# 方法上方@ststicmethod   方法参数可有可无
# 调用时:
#   类.方法名
#   对象.方法名

# 什么时候写静态方法?
#   无需调用对象中已封装的值

class Haha(object):
    def __init__(self, name):
        self.name = name
    #静态方法,如果方法无需使用对象中封装的值,那么就可以使用静态方法
    @staticmethod
    def func(a1, a2):
        print(a1 + a2)
    #类方法  cls是类,这样一来就是相当于自动传递了类这一参数
    @classmethod
    def output(cls):
        print(cls, '666666')
    #<class '__main__.Haha'> 666666


obj = Haha('xiaoming')
obj.func(2, 3)
Haha.output()
