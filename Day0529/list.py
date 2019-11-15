# 2019-05-29 16:58
from functools import reduce
lst = [1, '哈哈', "吼吼", [1,8,0,"百度"], ("我","叫", "元", "组"), "abc", {"我 叫":"dict字典"},{"我叫集合","集合"}]
# 列表是可以发生改变的,和字符串不一样
lst[2]= "这是第二个被改过的值"
print(lst)
# 列表的切片
lst = ["麻花藤", "王剑林", "⻢芸", "周鸿医", "向华强"]
print(lst[0:3])     # ['麻花藤', '王剑林', '马芸']
print(lst[:3])      # ['麻花藤', '王剑林', '马芸']
print(lst[1::2])    # ['王剑林', '周鸿医'] 也有步⻓长
print(lst[2::-1])   # ['⻢马芸', '王剑林林', '麻花藤'] 也可以倒着取
print(lst[-1:-3:-2])# ['向华强'] 倒着带步⻓长

# lst = []
# print(lst)
# while True:
#     content = input("Please input what you want,exit with Q")
#     if(content.upper()=='Q'):
#         break
#     lst.append(content)
# print(lst)

lst = ["马化腾","张福州","空肚饿"]
lst.insert(1,"小胖子")#在1的位置插入小胖子
print(lst)

lst.extend(["lala","zhuzhu"])
print(lst)

# pop, remove, clear, del
lst = ["麻花藤", "王剑林林", "李李嘉诚", "王富贵"]
print(lst)
deleted = lst.pop()         # 删除最后⼀一个
print("被删除的", deleted)
print(lst)
el = lst.pop(2)     # 删除2号元素
print(el)
print(lst)
lst.remove("麻花藤")   # 删除指定元素
print(lst)
lst.clear()
print(lst)
lst = ['askjb','asb','as','a']
del lst[1:3]
print(lst)

# 修改
lst = ["太⽩白", "太⿊黑", "五⾊色", "银王", "⽇日天"]
lst[1] = "太污"   # 把1号元素修改成太污
print(lst)
lst[1:4:2] = ["麻花藤", "哇靠"]     # 切⽚片修改也OK. 如果步⻓长不不是1, 要注意. 元素的个 数
print(lst)
lst[1:4] = ["李李嘉诚个龟儿子"]  # 如果切⽚片没有步⻓长或者步⻓长是1. 则不不⽤用关心个数
print(lst)

lst = ["太⽩白", "太⿊黑", "五⾊色", "银王", "⽇日天", "太⽩白"]
c = lst.count("太⽩白")     # 查询太⽩白出现的次数
print(c)

lst = [1,21,11,23,20]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)

def fn(x,y):
    return x*10+y
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

print(reduce(fn,map(char2num,'13562')))

def is_odd(n):
    return n % 2 == 1
l = [1,2,3,4,5,6,7]
filter(is_odd,l)
print(l)

