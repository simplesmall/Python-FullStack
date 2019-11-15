print('包')
#包:文件夹有一个__init__.py文件
#包:是几个模块的集合

#从包中导入模块
# import glance.api.policy as policy
#policy.get()
######常用的是下面这两种
# from glance.api import policy
#policy.get()

# from glance.api.policy import get
# get()
#直接导入一个包
#导入一个包
#   不意味着这个包下面的所有内容都是可以被使用的
#   导入一个包到底发生了什么
#       相当于执行了这个包下面的__init__.py文件

#相对导入
#必须放在包中被导入的调用才能正常的使用
#含有相对导入的文件不能被直接执行