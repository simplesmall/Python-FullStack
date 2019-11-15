def f1():
    print(11)
    x1 = yield 1
    print(22)
    x2 = yield 2
    print(33)

def f2():
    print(44)
    yield
    print(55)
    yield
    print(66)

v1 = f1()
v2 = f2()

# next(v1)    # v1.send(None)
# next(v2)    # v2.send(None)


ret = v1.send(None)
print(ret)
r2 = v1.send(999)
print(r2)
