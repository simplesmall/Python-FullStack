"""
一.回顾上次课内容
    1,基础知识点补充
     join()把一个列表转换成字符串
     split()切割,把字符串变成列表
     删除问题.
      list 和dict
      list删除在循环的时候不能直接删除的
      dict在循环的时候不要改变大小

      需要把要删除的内容保存在一个列表中,循环这个列表删除老列表
      fromkeys(a,b)把a中的每一个元素获取到和b组装成一个新的字典返回
    2.set集合:不重复,无序,内容必须可哈希(不可变)
    3.深浅拷贝
        1.赋值:没有创建新对象.两个对象指向同一个对象
        2.浅拷贝:拷贝第一层内容.创建了新对象 [:]  copy()
        3.深拷贝: 拷贝所有和当前对象相关联的类. deepcopy()

"""
print("文件操作")

# num = input("请输入三位数")
# s = 0
#
# # for c in num:
# #     s = int(c)**3+s
# # 等效于:
# s = int(num[0])**3 + int(num[1])**3 + int(num[2])**3
# if int(num)==s:
#     print("这是一个水仙花数")
# else:
#     print("不是")


from random import randint

r = randint(0, 20)
print(r)
count = 1
s = set()
# 此处不能由计数来实现set中的个数是因为set中元素不能重复,而
# 用len则可以忽略是否重复的问题
while len(s) < 7:
    r = randint(1, 36)
    s.add(r)
    count += 1
print(s)

# salary = int(input("请输入你的工资"))
# if salary <= 2000:
#     print("未到起征点")
# elif salary <= 4000:
#     print((salary-2000)*0.03)
# elif salary <= 6000:
#     print((salary-2000)*0.03+(salary-4000)*0.05)
# else:
#     print((salary-2000)*0.03+(salary-4000)*0.05+(salary-6000)*0.08)

a = 10
b = 4
# c = a
# a = b
# b = c
a, b = b, a
print(a, b)

lst = [3, 5, 4, 2, 1, 6, 8, 2, 4]
count = 0
while count < len(lst):  # 控制次数
    i = 0
    while i < len(lst) -  1:
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
        i += 1
    count += 1
print(lst)
