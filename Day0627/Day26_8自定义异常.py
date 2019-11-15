class MyException(Exception):
    def __init__(self,code,msg):
        self.code = code
        self.msg = msg
try:
    raise MyException(1000,'操作异常')
except MyException as e:
    print(e.code,e.msg,111)
except Exception as obj:
    print(obj,222)