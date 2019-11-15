print("ionf")

a = lambda n, m: n * n + m + 123
print(a(12, 12))

lst = [16, 45, 23, 2, 34, 12]
ll = sorted(lst)
ll = sorted(lst, reverse=True)
print(ll)

lst = ["张无忌", "张铁林", "赵敏", "小昭"]


def func(el):
    if el[0] == "张":
        return False
    else:
        return True


f = filter(func, lst)
# f = filter(lambda  el:el[0]!="张", lst)  #等效的
print("__iter__" in dir(f))  # 判断是否是可迭代对象

for e in f:
    print(e)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
f = filter(lambda x: x % 2 == 0, lst)
print(f)
print(list(f))

m = map(lambda x: x ** 2, lst)
print(list(m))
