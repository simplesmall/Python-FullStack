def buy():
    print('buy')
    name


def back():
    print('back')
    [][1]


def show():
    print('show')
    2 / 0


# 万能异常
def main():
    l = [('购物', buy), ('退货', back), ('查看订单', show)]
    while True:
        for num, i in enumerate(l, 1):
            print(num, i[0])

        num = int(input('num >>>'))
        print(l[num - 1])
        # 取得是函数名称,就是元组里面的位置0
        print('用户在选择了%s操作之后发生了不可知的错误' % l[num - 1][0])
        # 获取真实运行的函数
        # func = l[num-1][1]
        # func()
        try:
            l[num - 1][1]()
        # 万能异常,将异常情况as 成变量然后进行显示和操作
        except Exception as e:
            # 显示错误以及发生错误的行数
            print(e, e.__traceback__.tb_lineno)


# main()

# 万能异常 相当于 except Exception 永远放在最下面
try:
    name
    [][1]
    int('aa')
except:
    print('123')
finally:  # 即使遇到报错程序结束,也会先执行finally中的代码,然后再结束程序
    print("无论如何都会被执行")

# raise ValueError('你写的不对')

# 断言  assert
# 只能接受一个布尔值 满足条件向下走,不满足则抛出异常
assert 1 == 1
print('下来了')
