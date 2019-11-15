class Foo(object):
    def __init__(self, age):
        self.age = age

    def display(self):
        print(self.age)
        return 123


data_list = [Foo(8), Foo(9)]


# for item in data_list:
#     print(item.age, item.display())
# 8
# 8
# None
# 9
# 9
# None


class StackConfig(object):
    def __init__(self, num):
        self.num = num

    def changelist(self, request):
        print(self.num, request)

    def run(self):
        self.changelist(999)


class RoleConfig(StackConfig):
    def changelist(self, request):
        print('666')


# 构造函数自己没有则去父类里面寻找,找到以后就直接调用,
# 所以这里的效果相当于是在 RoleConfig中添加了 __init__函数而且是在里面赋值了 self.num = num
config_list = [StackConfig(1), StackConfig(2), RoleConfig(3)]
for item in config_list:
    print(item.num)
    item.changelist(12)
config_list[1].run()
config_list[2].run()


class AdminSite(object):
    def __init__(self):
        self._registry = {}

    def register(self, k, v):
        self._registry[k] = v
site = AdminSite()
print(len(site._registry))

site.register('range',666)
site.register('daniu',999)
print(len(site._registry))

site.register('lnk',StackConfig(19))
site.register('dat',StackConfig(20))