#需要从一个文件中使用哪个名字,就把这个名字导入进来
from my_module import name
print(type(name))
print('Name is',name)
from  my_module import func1
print(type(func1))
func1()

#导入多个名字 import red1,red2
#给导入的名字起别名 import red1 as red

from my_module import * #导入全部
print(name)
name = 'Justin'
print(name)
func1()

#__all__ 是一个列表,里面就是import *时的导入项参考
#且 __all__ 只能约束 * 导入时的导入内容