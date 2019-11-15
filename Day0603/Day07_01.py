li = ["李嘉诚", "麻花藤", "⻩海峰", "刘嘉玲"]
s = "_".join(li)
print(s)
li = "⻩花⼤闺女"
s = "_".join(li)
print(s)

li = [11, 22, 33, 44]
for e in li:
    li.remove(e)
print(li)
# for的运⾏行行过程.会有⼀一个指针来记录当前循环的元素是哪⼀一个, ⼀一开始这个指针指向第0
# 个.然后获取到第0个元素.紧接着删除第0个.这个时候.原来是第⼀一个的元素会⾃自动的变成
# 第0个.然后指针向后移动⼀一次, 指向1元素.这时原来的1已经变成了了0, 也就不会被删除了了.

li = [11, 22, 33, 44]
# for i in range(0, len(li)):
#     del li[i]
# print(li)

# i= 0, 1, 2  删除的时候li[0] 被删除之后. 后⾯面⼀一个就变成了了第0个.
# 以此类推. 当i = 2的时候. list中只有⼀一个元素. 但是这个时候删除的是第2个 肯定报错啊

for i in range(0, len(li)):  # 循环len(li)次, 然后从后往前删除
    li.pop()
print(li)

li = [11, 22, 33, 44]
del_li = []
print(li)
for e in li:
    del_li.append(e)
for e in del_li:
    li.remove(e)
print(li)

dic = dict.fromkeys(["jay", "JJ"], ["周杰伦", "马化腾"])
print(dic)
dic.get("jay").append("胡八一")
print(dic)

# 把要删除的元素暂时先保存在⼀一个list中, 然后循环list, 再删除
dic = {'k1': 'alex', 'k2': 'wusir', 's1': '⾦老板'}
dic_del_list = []  # 删除key中带有'k'的元素
for k in dic:
    if 'k' in k:
        dic_del_list.append(k)
for el in dic_del_list:
    del dic[el]
print(dic)

tup = {1,2,3,'as','qwe','qsc'}
print(tup)
l1 = list(tup)
print(l1)
l2 = tuple(l1)
print(l2)
print(tup,l1,l2)
