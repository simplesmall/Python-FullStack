print("Homework explain")
# 取出数组中的奇数位
lst = ["熊大", "喜洋洋", "葫芦娃", "小哪吒", "容嬷嬷"]


def func(lst):
    result = []
    for i in range(len(lst)):
        if i % 2 == 0:
            result.append(lst[i])
    # return result
    return lst[1::2]


# ret =func(("熊大", "喜洋洋", "葫芦娃", "小哪吒", "容嬷嬷","kas","ashsvf"))
ret = func(lst)
print(ret)


def length(a):
    return len(a) > 5


print(length("123456"))


def count(s=""):
    digit = 0
    alpha = 0
    blank = 0
    other = 0
    for i in s:
        if i.isdigit():
            digit += 1
        elif i.isalpha():  # 中文竟然是计数在alpha里面
            alpha += 1
        elif i == ' ':
            blank += 1
        else:
            other += 1
    return digit, alpha, blank, other


print(count("123 asd asdjkh asjk@@3#$"))


def diff(a, b):
    return a if a > b else b


# 三目运算符
print(diff(2, 1))


def searchDic(dic):
    newdic = {}
    for k, v in dic.items():
        if len(v) > 2:
            s = v[0:2]
            newdic[k] = s
        else:
            newdic[k] = v
    return newdic


print(searchDic({"a": "123", "b": "as", "c": "32425"}))


def lst(s):
    dic = {}
    if type(s) == list:
        for i in range(len(s)):
            dic[i] = s[i]
        return dic
    else:
        print("不是列表.")


print(lst(["123", "jhas", "ashu"]))

# def add(name,gender,age,edu):
#     with open("student_msg",mode="a",encoding="utf-8") as f:
#         f.write(name+'_'+gender+'_'+age+'_'+edu+'\n')
# name = input("Name please:")
# gender = input("Gender please:")
# age = input("Age please:")
# edu = input("Education level please:")
# print(add(name,gender,age,edu))

