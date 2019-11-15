import re

def calculatoradd(string):
    lst = []
    sum = 0
    string = string.strip()
    lst = string.split('+')
    for i in range(len(lst)):
        lst.append(lst[i])
        sum += int(lst[i])
    return sum

print(calculatoradd('1+2+3'))

# 原子型操作
def atom_cal(exp):
    if '*' in exp:
        a, b = exp.split('*')
        return str(float(a) * float(b))
    elif '/' in exp:
        a, b = exp.split('/')
        return str(float(a) / float(b))


# 解决乘除法符号匹配以及表达式的返回
def format_exp(exp):
    exp = exp.replace('--', '+')
    exp = exp.replace('+-', '-')
    exp = exp.replace('-+', '-')
    exp = exp.replace('++', '+')
    return exp


# 乘除法
def mul_div(exp):
    # 匹配乘除法的正则表达式
    while True:
        ret = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?', exp)
        if ret:
            atom_exp = ret.group()
            # 原子操作将乘除法
            res = atom_cal(atom_exp)
            # 用新的字符串替换旧的字符串
            exp = exp.replace(atom_exp, res)
            print(atom_exp)
        else:
            return exp


# 加减法
def add_sub(exp):
    # 找出所有要执行加减的的单个元素,用?:取消分组优先
    ret = re.findall('[+-]?\d+(?:\.\d+)?', exp)
    print(ret)  # 将得出的 ['2', '+22.0', '+3', '+0.8'] 逐个取出做加法完成最后的运算
    exp_sum = 0
    # 字符串转换成float并累加
    for i in ret:
        exp_sum += float(i)
    return exp_sum


# 计算器
def cal(exp):
    # 解决乘除法
    exp = mul_div(exp)
    # 格式化输出运算符
    exp = format_exp(exp)
    print(exp)
    # 将置换出来的每个单个式子做加法
    exp_sum = add_sub(exp)
    print(exp_sum)
    return exp_sum


cal('2-1*-22+3-4/-5+20/4')
print(2 - 1 * -22 + 3 - 4 / -5 + 20 / 4)

#带()括号的计算表达式
def main(exp):
    #将表达式里面的空格去掉
    exp = exp.replace(' ', '')
    print(111, exp)
    while True:
        #取出括号里面的运算式并计算出然后带入到表达式里面替换
        ret = re.search('\([^()]+\)', exp)
        if ret:
            inner_bracket = ret.group()
            #括号里面的内容 (3+12-2*1.0+4/2.0)
            print('ret.group is:',ret.group())
            res = str(cal(inner_bracket))
            print(inner_bracket, res)
            exp = exp.replace(str(inner_bracket), res)
            exp = format_exp(exp)
        else:
            break
    print('main output ', exp)
    return cal(exp)


main('(3+12-2*(3-2)+4/(1+1))')
print('Original output is :', (3 + 12 - 2 * (3 - 2) + 4 / (1 + 1)))
