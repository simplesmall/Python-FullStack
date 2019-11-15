# print("2019-05-30")
import functools
def now():
    print("20190530")
f = now
f()
print(f.__name__)
print(now.__name__)
print("################")
# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('decorator的高阶函数')
now()
print(int('123123',base=8))