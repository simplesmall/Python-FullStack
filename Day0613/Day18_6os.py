import os
#mkdir 可以创建单级目录,而mkdirs可以创建多级目录
# os.mkdir('dir1')
# os.makedirs('dir2/dir3')
print('123r4')

#只能删空文件夹
# os.rmdir('dir1')
# os.removedirs('dir2/dir3')

# print(os.listdir())

#路径拼接  os.listdir  /  os.path.join
file_lst = os.listdir('D:\FullStackD\Stack15\Day0613')
for path in file_lst:
    print(os.path.join('D:\FullStackD\Stack15\Day0613',path))

#exec/eval 执行的是字符串数据类型的python 代码
#os.system 和os.popen 是执行字符串数据类型的python 代码
# os.system('dir')
ret = os.popen('dir') #适合做查看类工作
print(ret.read())

#当前工作目录
#不是指当前文件所在的目录.而是当前文件时在哪个目录下执行的
print(os.getcwd())

#切换当前工作目录
os.chdir('D:\FullStackD\Stack15\Day0612')
print(os.getcwd())

