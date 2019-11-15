class BaseMessage(object):
    """
    必须继承BaseMessage(),然后其中必须编写send方法.用于完成具体业务逻辑
    """
    def send(self):
        # raise Exception()
        raise NotImplementedError("send 方法未被重写产生错误")
###  约束其派生类,保证派生类中必须编写send方法,不然执行可能就会报错

class Email(BaseMessage):
    def send(self):
        print('Email send')


class Wechat(BaseMessage):
    def send(self):
        print('Wechat send')


class Msg(BaseMessage):
    def send(self):
        print('Msg send')


def func(arg):
    """
    报警通知的功能
    :param arg:
    :return:
    """
    arg.send()


obj = Msg()
obj.send()
