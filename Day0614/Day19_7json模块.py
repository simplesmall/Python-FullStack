import json

dic = {'key': 'value', 'key2': 'value'}

ret = json.dumps(dic)  # 序列化
print(dic, type(dic))
print(ret, type(ret))
# {'key': 'value', 'key2': 'value'}
# {"key": "value", "key2": "value"}
# {'key': 'value', 'key2': 'value'} <class 'dict'>
res = json.loads(ret)
print(res, type(res))  # 反序列化

# 问题1 改变了数据类型 从 1 到了 '1'
dic = {1: 'value', 2: 'value'}
ret = json.dumps(dic)  # 序列化
print(dic, type(dic))
print(ret, type(ret))
# {1: 'value', 2: 'value'} <class 'dict'>
# {"1": "value", "2": "value"} <class 'str'>
# {'1': 'value', '2': 'value'} <class 'dict'>
res = json.loads(ret)
print(res, type(res))  # 反序列化

# 问题2 改变了数据类型,还原回来的时候全部转换为[]了,之前是() 从 1 到了 '1'
dic = {1: [1, 2, 3], 2: (4, 5, 'aa')}
ret = json.dumps(dic)  # 序列化
print(dic, type(dic))
print(ret, type(ret))
# {1: [1, 2, 3], 2: (4, 5, 'aa')} <class 'dict'>
# {"1": [1, 2, 3], "2": [4, 5, "aa"]} <class 'str'>
# {'1': [1, 2, 3], '2': [4, 5, 'aa']} <class 'dict'>
res = json.loads(ret)
print(res, type(res))  # 反序列化

dic = {'alex': 'zhazha', 'bill': 'shuashua'}
ret = json.dumps(dic)
# with open('json_file','a') as f:
#     f.write(ret)

# with open('json_file', 'r') as f:
#     str_dic = f.read()
# dic = json.loads(str_dic)
# print(dic)

with open('json_file', 'r') as f:
    dic = json.load(f)
print(dic)
