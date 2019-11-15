import random

print(random.random())  # 取值0-1之间的随机小数
print(random.uniform(1, 2))  # 取值a-b之间的随机小数

print(random.randint(1, 5))  # 取值a-b之间的随机int数 [a,b]
print(random.randrange(1, 5))  # 取值a-b之间的随机int数  [1,2)

l = ['a', 'b', (1, 2, 3), 678]
print(random.choice(l))
print(random.sample(l, 3))

# 打乱顺序 在原列表基础上修改 节省空间
random.shuffle(l)
print(l)


# 4位的数字验证码
def code(n=6):
    s = ''
    for i in range(n):
        num = random.randint(0, 9)
        s += str(num)
    return s


print(code(4))
print(code())


# 字母/数字兼容的函数
def six(n=6, alpha=True):
    s = ''
    for i in range(n):
        # 生成随机的字母,数字各一个
        num = str(random.randint(0, 9))  # 数字
        if alpha:
            alpha = chr(random.randint(65, 90))  # 大写字母
            belt = chr(random.randint(97, 122))  # 小写字母
            num = random.choice([num, alpha, belt])
        s += num
    return s

print(six(4, False))
print(six(8))
print(six(alpha=False))

# 发红包
