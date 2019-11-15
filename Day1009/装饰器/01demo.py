
# 闭包函数:内层函数调用外层函数的环境变量,这样的函数叫闭包函数
def foo():
    x=1
    def inner():
        print(x)
    return inner

# print(foo())
# print(foo().__closure__[0].cell_contents)

a = 1
y = 2
if a == 1:
    a += 1
    y += 2
# print(a, y)

def login(func):
    def inner():
        user = input("user>>>")
        pwd = input("pwd>>>>")
        if user=="alex" and pwd =="123":
            print("success!")
            func()
        else:
            print("error")
    return inner
@login # index= login(index)
def index():
    print("This is index!")

# index()

################   练习  #################
def cost(func):
    def inner():
        import time
        s1 = time.time()
        func()
        print("Processing cost time:",time.time()-s1)
    return inner
@cost
def add():
    ret = 1;
    for i in range(3000000):
        ret+=i
    print(ret)

# add()

@cost 
def counter():
    import time
    ret = 1
    for i in range(10):
        time.sleep(0.3)
        ret+=i*2
    print(ret)
counter()