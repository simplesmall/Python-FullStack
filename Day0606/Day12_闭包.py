#在内层函数中访问外层变量
#克服全局变量的不稳定
#   1.可以保护你的变量不受侵害
#   2.可以让一个变量常驻内存
# 查看函数是否是闭包 .__closure__打印出cell字样的东西则是闭包
def outer():
    a = 10 #常驻内存,为了inner执行的时候有值
    def inner():
        print(a)
    inner()
outer()

from  urllib.request import  urlopen
s = urlopen("http://www.xiaohuar.com/").read()
print(s)

def outer():
    s = urlopen("http://www.tcig.cn").read()
    def getContent():
        return  s
    return getContent
print("爬取内容...")
pa = outer()

ret = pa()
print(ret)

ret = pa()
print(ret)

ret = pa()
print(ret)