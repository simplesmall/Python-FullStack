dic = {123: 456, True: 999, "id": 1, "name": 'sylar', "age": 18, "stu": ['帅哥', '美女'], (1, 2, 3): '麻花藤'}
print(dic[123])
print(dic[True])
print(dic['id'])
print(dic['stu'])
print(dic[(1, 2, 3)])

# 不合法
# dic = {[1, 2, 3]: '周杰伦'}   # list是可变的. 不能作为key
# dic = {{1: 2}: "哈哈哈"}     # dict是可变的. 不能作为key
# dic = {{1, 2, 3}: '呵呵呵'}    # set是可变的, 不能作为key

dic = {}
dic['name'] = '周润发'
dic['age'] = 18
print(dic)
dic.setdefault('李嘉诚')
dic.setdefault('李嘉诚', '房地产')
print(dic)

rec = dic.pop('name')
print(dic)
del dic['李嘉诚']
print(dic)
ret = dic.popitem()
print(dic)
dic.clear()

dic = {"id": 123, "name": 'sylar', "age": 18}
dic1 = {"id": 456, "name": "麻花藤", "ok": "wtf", "123": "45667"}
dic.update(dic1)  # 把dic1中的内容更更新到dic中. 如果key重名. 则修改替换. 如果不不存 在key, 则新增.
print(dic)
print(dic1)

print(dic['name'])  # print(dic['sylar'])     # 报错
print(dic.get("ok"))
print(dic.get("sylar"))  # None
print(dic.get("123"))  # ⽜牛B

dic = {"id": 123, "name": 'sylar', "age": 18, "ok": "科比"}
print('1111111111111')
print(dic.keys())  # dict_keys(['id', 'name', 'age', 'ok']) 不不⽤用管它是什什么.当 成list来⽤用就⾏行行
for key in dic.keys():
    print(key)
print(dic.values())  # dict_values([123, 'sylar', 18, '科⽐比']) ⼀一样. 也当 list来⽤用
for value in dic.values():
    print(value)
print(
    dic.items())  # dict_items([('id', 123), ('name', 'sylar'), ('age', 18), ('ok', '科⽐比')]) 这个东⻄西也是list. 只不不过list中装的是tuple
for key, value in dic.items():  # ?? 这个是解构
    print(key, value)

# 解构
a, b = 1, 2
print(a, b)
(c, d) = 3, 4
print(c, d)
e, f = [1, 2]  # 解构的时候一定要注意数量匹配
print(e, f)

# 字典的嵌套
dic1 = {"name": "汪峰",
        "age": 18,
        "wife": {
            "name": '章⼦怡',
            "age": 28},
        "children": ['第⼀个⽑毛孩子', '第⼆个毛孩⼦'],
        "desc": '峰哥不不会告我吧. 没关系. 我想上头条的'}
print(dic1.get("wife").get("name"))
print(dic1['wife']['age'])
print(dic1["children"])

dic1 = {'name': ['alex', 2, 3, 5],
        'job': 'teacher',
        'oldboy': {'alex': ['python1', 'python2', 100]}
        }
dic1['name'].append('musir')
print(dic1['name'])
print(dic1['name'][0].capitalize())
dic1['oldboy']['老男孩']= 'linux'
print(dic1['oldboy'])
# dic1['oldboy'].remove('python2')
print(dic1['oldboy']['alex'][1])
dic1['oldboy']['alex'].remove('python2')
print(dic1)

a = 'alex@'
b = 'alex@'
print(a is b)

a = 5//2
b = 2
print(a is b)

a = 'a'*21
b = 'a'*21
print(a is b)

a = -6
b = -6
print(a is b)

a = 267
b = 267
print(a is b)
print(a == b)

print('11111111111')
s = 'alex'
print(s.encode('utf-8'))    # 编码 encode('utf-8') utf-8 是指定要编码成什么样的编码类型


s = '饿了'
s1 = s.encode('gbk')      #b'饿了吗'    #b'\xe9\xa5\xbf\xe4\xba\x86\xe5\x90\x97'
print(s.encode('gbk'))                 #b'\xb6\xf6\xc1\xcb\xc2\xf0'
print(s1)
# print(s1.decode('utf-8'))

#列表
li =[1,2,3]
li2 =[1,2,3]
print(li is li2)  #False
#元组
tu =(1,2,3)
tu1 =(1,2,3)
print(tu is tu1)   # False
#字典
dic1 = {'name':'alex'}
dic = {'name':'alex'}
print(dic1 is dic)    #False