a = 10
def func():
    global  a  #可以把全局中的内容引入到函数内部 没有则表示在全局创建一个变量
    a = 20

#执行函数使得global这一函数生效
func()
print(a)

def outer():
    a = 10
    def inner():
        nonlocal a #寻找外层函数中离它最近的那个变量,如果再全局之内一层还没找到就会报错,不会到最外层的全局变量
        # global a #寻找外层函数中离它最近的那个变量,如果再全局之内一层还没找到就会报错,不会到最外层的全局变量
        a = 30
        print(id(a))
    inner()
    print(id(a))
outer()