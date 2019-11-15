#py .dll文件 zip文件
#如何自己写一个模块
import my_module
import my_module  as m
print(my_module.name)
print(my_module.func1)
print(my_module.func1())
print(m.name)

def func(dic,t = 'json'):
    if t == 'json':
        import json as aaa
    elif t == 'pickle':
        import pickle as aaa
    return aaa.dumps(dic)
