#isdir()  isfile()

import os
import time
te = os.getcwd()
print(te)
print(os.path.getatime(te))  #最后访问时间
print(os.path.getmtime(te))  #最后修改时间
print(os.path.getsize('D:\FullStackD\Stack15\Day0614\Day19_4os.py'))  #查看文件大小,单位是字节
print(os.path.getsize('D:\FullStackD\Stack15'))  #查看文件大小,单位是字节,每一个文件夹最小是4096

#统计文件夹大小
#递归版本
# def func(path):
#     sum = 0
#     name_list = os.listdir(path)
#     for name in name_list:
#         path_abs = os.path.join(path,name)
#         if os.path.isdir(path_abs):
#             size_child = func(path_abs)
#             sum += size_child
#         else:
#             sum += os.path.getsize(path_abs)
#     return  sum
# # func('This is all:'+str(func(os.getcwd())))
# func('This is all:'+str(func('D:\FullStackD\Stack15')))

#循环版本
# l = [r'D:\FullStackD\Stack15']
# size_sum = 0
# while 1:
#     path = l.pop()
#     path_list = os.listdir(path)
#     for name in path_list:
#         abs_path = os.path.join(path,name)
#         if os.path.isdir(abs_path):
#             l.append(abs_path)
#         else:
#             size_sum += os.path.getsize(abs_path)
# print(size_sum)

# exec('字符串数据类型的python代码')
# eval('执行字符串数据类型的python代码')
#
# os.system('执行字符串数据类型的操作系统命令')
# os.popen('执行字符串数据类型的操作系统命令,并返回结果')

# getcwd 获取当前执行 命令的时候所在的目录
# chdir  修改当前执行命令的时候所在的目录
ret = os.popen('dir').read()
print(ret)