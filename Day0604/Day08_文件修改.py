# 引入模块
import os
import  time
# f1 = open("todoList",mode="r",encoding="utf-8")
with open("todoList",mode="r",encoding="utf-8") as f1,\
    open("todoList_one",mode="w",encoding="utf-8") as f2:
    for line in f1:
        line = line.replace("alex","sb")
        f2.write(line)

# time.sleep(3)

# 删除文件
os.remove("todoList")
os.rename("todoList_one","todoList")

lst = []
with open("test.log",mode="r",encoding="utf-8") as f:
    first = f.readline().strip().split(",")
    for line in f:
        dic = {}
        ls = line.strip().split(",")
        for i in range(len(first)):
            dic[first[i]]=ls[i]
        lst.append(dic)
print(lst)