# if hasattr(handler,val)
# getattr(handler,val)
class Foo(object):
    country = '中国'

    def func(self):
        pass


obj = Foo()
v = getattr(Foo, 'country')
print(v)
v1 = getattr(Foo, 'func')  # Foo.func 根据字符串为参数,去类中寻找与之同名的成员
print(v1)
v = getattr(obj, 'func')    #obj.func  根据字符串为参数,去对象中寻找与之同名的成员
print(v)

class Account(object):
    func_list = ['login', 'logout', 'register']
    def login(self):
        print('login')
    def logout(self):
        print('logout')
    def register(self):
        print('register')
    def run(self):
        while True:
            print("""
                请输入要执行的操作:
                    1.登录
                    2.注销
                    3.注册
                    4.退出
            """)
            choice = int(input('请输入要执行的操作序号'))
            if choice == 4:
                break
            func_name = Account.func_list[choice-1]
            #以反射的方式来找到要执行的函数,与对象名拼接完成要执行的函数的
            # func = getattr(Account,func_name)
            # func(self)
            func = getattr(self, func_name)
            func()

obj = Account()
obj.run()