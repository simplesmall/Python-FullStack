def func():
    print("哇哈哈")
    yield 1
    print("呵呵呵")

gen = func() #不会执行函数,拿到的是生成器
ret = gen.__next__()
print(ret)
# gen.__next__()
#函数中如果有yield,函数就是生成器函数,生成器函数()获取的是生成器,这个时候不执行函数
#yield:相当于return 可以返回数据,但是yield不会彻底中断函数.分段执行函数

# def order():
#     lst = []
#     for i in range(10000):
#         lst.append("衣服"+str(i))
#     return lst
# ll = order()
# print(ll)

