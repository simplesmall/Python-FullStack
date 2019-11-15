import sys
print(sys.argv) #argv的第一个参数是python这个命令后面的值
# usr = sys.argv[1]
# pwd = sys.argv[2]
# if usr=='alex' and pwd =='1234':
#     print("登录成功")
# else:
#     exit()

# print(sys.path)
# print(sys.modules) #导入到内存中的所有模块的名字:这个模块在内存中的地址
import re
print(sys.modules['re'].findall('\d','cgvh324'))

