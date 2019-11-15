def func():
    print("我是第一")
    a  = yield  123
    print(a)
    print("我是第二")
    yield 456
    print("我是第三")
    yield 789
    print("最后一段")
    yield 77 #最后收尾一定是yield

g = func()
print(g.__next__())
print(g.send("煎饼果子"))
print(g.__next__())
print(g.__next__())

#推导式
lst = ["python"+str(i) for i in range(1,16)]
print(lst)

def add(a,b):
    return a + b
def test():
    for r in range(4): 
        yield r
g = test()
for n in [1,10,5]:
    g = (add(n,i) for i in g)
print(list(g))