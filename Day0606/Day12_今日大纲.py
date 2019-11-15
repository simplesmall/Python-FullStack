"""
一.昨日内容回顾
二.作业
三.今日主要内容:
    1.函数名的应用(第一类对象)

    2.闭包
    3.迭代器
"""


def func():
    print("123")


print(func)


def addfunc(*args):
    # sum = 0
    # for i in args:
    #     sum+=i
    print(sum(args))


addfunc(1, 2, 3)
print(sum([1, 2, 3, 4]))  # sum可以直接拿来用,参数里面使用的是可迭代对象


def strtest(lst=[1, "alex", 'wusir']):
    s = ""
    for el in lst:
        s = s + str(el) + "_"
    return s.strip("_")


print(strtest())
print(max([1, 5, 7, 234, 978, 324, 222]))


def complex():
    result = []
    huase = ["红心", "黑桃", "草花", "方片"]
    dianshu = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    for hua in huase:
        for dian in dianshu:
            result.append((hua, dian))
    return result


print(complex())


def wrapper():
    def inner():
        print(666)

    return inner


ret = wrapper()
print(ret)
ret()


def extendList(val, list=[]):  # 默认值如果是可变的数据类型,每次使用的时候都是同一个
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print(list1)
print(list2)
print(list3)


for i in range(1,10):
    for j in range(1,i+1):
        print("%s x %s = %s"%(i,j,i*j),end=" ")
    print("") #打印默认换行