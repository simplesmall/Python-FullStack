"""
    面向对象

    网络编程
    并发编程

今日内容:
    1.函数式编程和面向对象的对比
    2.面向对象代码如何编写
    3.面向对象三大特性:封装/继承/多态
"""


class Message:
    def eamil(self, em, text):
        """

        :param em:
        :param text:
        :return:
        """
        print(em, text)

    def msg(self, tel, text):
        """

        :param tel:
        :param text:
        :return:
        """
        print(tel, text)

    def wechat(self, num, text):
        """

        :param num:
        :param text:
        :return:
        """
        print(num, text)


if 1 == 1:
    obj = Message()
    obj.eamil('alex@qq.com', '来呀,快活呀')
    obj.msg('18872098712', '你收到了一条短信')
    obj.wechat('wxid_jianxiao', '请查收你的消息')


# 一个在__init__里面封装一些东西的例子

# 将数据封装到对象中,以供自己在方法中调用
class FileHandler:
    def __init__(self, filepath):
        self.file_path = filepath
        self.f = open(self.file_path, 'rb')

    def read_first(self):
        # self.f.read()
        # ...
        pass

    def read_last(self):
        # self.f.read()
        pass

    def read_second(self):
        # self.f...
        pass


obj = FileHandler('D:\FullStackD\Stack15\Day0618\Day22_0.py')
obj.read_first()
obj.read_last()
obj.read_second()
obj.f.close()


#将数据进行封装,以供别人调用
def new_func(arg):
    arg.k1
    arg.k2
    arg.k6


class Foo:
    def __init__(self, k1, k2, k6):
        self.k1 = k1
        self.k2 = k2
        self.k6 = k6


obj = Foo(111, 222, 333)
new_func(obj)
