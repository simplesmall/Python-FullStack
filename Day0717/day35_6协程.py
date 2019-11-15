import greenlet

def f1():
    print(11)
    gr2.switch()
    print(22)
    gr2.switch()

def f2():
    print(33)
    gr1.switch()
    print(44)

gr1 = greenlet.greenlet(f1)
gr2 = greenlet.greenlet(f2)

gr1.switch()