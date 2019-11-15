# def registyer():
#     print("Welcome register")
#     while 1:
#         username = input("Username please:")
#         password = input("Password please:")
#         f = open("db.log",mode="r+",encoding="utf-8")
#         for line in f:
#             if username == line.split("@@")[0]:
#                 print("Username already exist,enter other please:")
#                 break
#             else: #没注册过
#                 f.write(username+"@@"+password+"\n")
#                 print("Register successful")
#                 return
#
# registyer()

# 函数名就是一个变量
def func():
    print("A single variable")


func()
print(func)
func = 3
print(func)


# 函数名可以作为参数传递给函数
def my():
    print("我是my")


def proxy(fn):  # 代理模式,装饰器
    fn()


proxy(my)


def func1():
    print("我是func1")

def func2():
    print("我是func2")

def funcall(fn,gn):
    print("Before progress")
    fn()
    gn()
    print("After progress")

funcall(func1,func2)

def funcin():
    print("我是funcin")
    a = 10
    def inner():
        print("我是inner")
    return inner
print(funcin()())
ret = funcin()
ret()


