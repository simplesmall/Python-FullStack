# * 在这里表示接收位置参数的动态传参
def chi(*food):
    print(food)


chi("spagiter", "apple", "orange")


# 先位置参数,然后再动态参数

# 关键字的动态传参
def can(**food):
    print(food)


can(food="zhu", dog="gou")


# 无敌传参
def canshu(*food, **good):
    """
    函数注释之动态传参和关键字传参
    :param food:动态传参
    :param good:关键位置的动态传参,使用键值对的字典形式传值
    :return:返回传入的变量值
    """
    print(food, good)


canshu("zhugou", "buru", "de", da="xiang", xiao="chongwu")
print(canshu.__doc__)  # 输出显示函数的文档

# 顺序
# 位置参数,*args,默认值参数,**args
# 以上参数可以随意搭配使用
"""
1.实参:
    位置参数
    默认值参数
    混合参数(位置,关键字)
2.形参:
    位置参数
    默认值参数
    动态传参:
        *args:位置参数动态传参
        **kwargs:关键字参数动态传参
    顺序:位置,*args,默认值,**kwargs
"""


def dasan(*food):  # 聚合,位置参数
    print(food)


lst = ["鸡蛋", "油条", "豆浆", "火腿肠"]
dasan(*lst)  # 打散.把list tuple set str进行迭代打散


# 聚合成关键字参数
def args(**kwargs):
    print(kwargs)


dic = {"name": "alex", "age": 18}
# 打散成关键字参数
args(**dic)

print(globals())  # 可以查看全局作用域中的内容


def local():
    a = 10
    print('111', locals())  # 查看当前作用域中的内容


local()
