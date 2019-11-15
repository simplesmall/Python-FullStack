s = {"周杰伦", "周杰伦", "周星星"}
print(s)
# set 中元素是不重复的且是无序的
# 给list去重复
lst = [45, 5, "哈哈", 45, '哈哈', 50]
lst = list(set(lst))  # 把list转换成set, 然后再转换回list
print(lst)

s = {"刘嘉玲", '关之琳', "王祖贤", "王祖贤"}
print(s)
s.add("郑裕玲")
# 重复的内容不不会被添加到set集合中
print(s)
s = {"刘嘉玲", "关之琳", "王祖贤"}
s.update("麻花藤")  # 迭代更新
print(s)
s.update(["张曼玉", "李若彤", "李若彤"])
print(s)

# s = {"小伙伴", "大货版", "老伙伴"}
# print(s)
# item = s.pop()
# print(s)
# print(item)
# s.remove("小伙伴")
# print(s)
# s.clear()
# print(s)

# set 集合因为没有索引所以不能用修改,要修改的话应该删除一个要修改的数据然后添加进去
s = {"xiao", "zhong", "da"}
print(s)
s.remove("xiao")
print(s)
s.add("feichangxiao")
print(s)

for el in s:
    print(el + 'Bingo!!!')

# 交集并集
s1 = {"刘胡兰", "李云龙", "岳飞"}
s2 = {"岳飞", "李四光", "董存瑞", }
# 交集
print(s1 & s2)
print(s1.intersection(s2))

# 并集
print(s1 | s2)
print(s1.union(s2))

# 差集
print(s1 - s2)
print(s1.difference(s2))

# 反交集  两个集合中单独存在的数据
print(s1 ^ s2)
print(s1.symmetric_difference(s2))

s1 = {"刘胡兰", "李云龙", "岳飞"}
s2 = {"刘胡兰", "李云龙", "岳飞", "张三丰"}

# 子集
print(s1 < s2)
print(s1.issubset(s2))

# 超集
print(s1 > s2)
print(s1.issuperset(s2))
# set集合本⾝身是可以发⽣生改变的. 是不可hash的.
# 我们可以使⽤用frozenset来保存数据. frozenset是不可变的. 也就是⼀一个可哈希的数据类型
s = frozenset(["赵本⼭", "刘能", "⽪长⼭", "长跪"])
dic = {s: '123'}  # 可以正常使⽤用了了
print(dic)

# 深拷贝
lst1 = ["⾦⽑狮王", "紫衫龙王", "⽩眉鹰王", "⻘翼蝠王"]
lst2 = lst1
print(lst1)
print(lst2)
lst1.append("杨逍")
print(lst1)
print(lst2)
print(id(lst1), id(lst2))
# 对于list, set, dict来说, 直接赋值. 其实是把内存地址交给变量量.
# 并不是复制⼀一份内容. 所以. lst1的内存指向和lst2是⼀一样的. lst1改变了了, lst2也发⽣生了了改变

# 浅拷⻉
lst1 = ["何炅", "杜海涛", "周渝⺠"]
lst2 = lst1.copy()
lst1.append("李嘉诚")
print(lst1)
print(lst2)
print(id(lst1), id(lst2))

lst1 = ["何炅", "杜海海涛", "周渝⺠民", ["麻花藤", "⻢马芸", "周笔畅"]]
lst2 = lst1.copy()
lst1[3].append("⽆无敌是多磨寂寞")
print(lst1)
print(lst2)
print(id(lst1[3]), id(lst2[3]))

a = [1, 2]
a[1] = a
print(a[1])

#浅拷贝
lst1 = [1,2,3,4]
lst2 = lst1[:]
lst1.append(5)
print(lst1)
print(lst2)
print(id(lst1),id(lst2))
#拷贝
lst3 = lst1.copy()
print(lst3)
print(id(lst1),id(lst3))
lst1.append(6)
print(lst1,lst3)

lst1 = ["zi","bai","jin","qing",["张无忌","赵敏","周芷若"]]
lst2 = lst1.copy()
print(lst1)
print(lst2)
print(id(lst1),id(lst2))
lst1[4].append("小昭")
print(lst1)
print(lst2)
print(id(lst1[4]),id(lst2[4]))

#深拷贝
import  copy
lst2 = copy.deepcopy(lst1)
print(id(lst1[4]),id(lst2[4]))
lst1[4].append('1')
print(lst1)
print(lst2)

# 1.赋值操作,没有创建新对象
# 2.没拷贝,只拷贝第一层内容. [:]   copy
# 3.深拷贝.把这个对象内部的内容全部拷贝一份.引入copy模块,deepcopy()