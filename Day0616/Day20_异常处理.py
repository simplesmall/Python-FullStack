# name
# 错误的追溯
# 错误类型 错误类型是有限的  具体的提示

print("异常处理")
# NameError name
# IndexError [][1]
# 空字节取key   KeyError {}['key']
# pickle.load() EOFError
# FileNotFoundError   open('aa')
# ModuleNotFoundError import aaaa
# ValueError int('asdjk')
# 语法错误 SyntaxError
# if

# 什么时候最容易出异常
# 当你处理的内容不确定的时候
# 有用户参与
# 有外界数据接入:从文件中读 从网络上获取

l = ['login', 'register']
for num, i in enumerate(l, 1):
    print(num, i)
try:
    num = int(input("Input num:"))
except ValueError:
    print("I have it")
print(l[num - 1])

#多分支except 可以接收解决不同类型错误
