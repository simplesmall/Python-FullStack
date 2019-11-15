import os
#返回当前运行目录的规范化路径
#能够给能找到的相对路径改成绝对路径
print(os.path.abspath(os.getcwd()))

path = os.path.split('D:\FullStackD\Stack15\Day0613')
path1 = os.path.split('D:/FullStackD/Stack15/Day0613')
print(path)
print(path1)
#split 的第一元素和第二元素分别为  dirname() 和 basename()