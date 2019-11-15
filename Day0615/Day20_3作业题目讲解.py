import os


# 写一个函数,接收一个参数,如果是文件,就执行这个文佳,如果是文件夹,就执行这个文件夹下的所有.py文件

def func(path):
    # 先判断这个path是文件夹还是文件
    # 如果是文件
    #     .py文件结尾的
    if os.path.isfile(path) and path.endswith('.py'):
        os.system('D:\FullStackD\env\Scripts\python.exe %s' % path)
    #           执行这个文件:os.system('python %s' %path)
    # 如果是文件夹
    elif os.path.isdir(path):
        #      查看这个文件夹下的所有内容 listdir
        for name in os.listdir(path):
            abs_path = os.path.join(path, name)
            #      如果这个文件 .py结尾的
            if abs_path.endswith('.py'):
                #       执行这个文件
                os.system('D:\FullStackD\env\Scripts\python.exe %s' % abs_path)


# func('D:/FullStackD/Stack15/Day0603')

# 2 写一个函数接收两个参数,把参数一的文件copy到参数二的位置
def copy(path1, path2):
    # 获得文件名称(不包括前面的位置索引)
    filename = os.path.basename(path1)
    print(filename)
    if os.path.isdir(path2) and os.path.isfile(path1):
        # 采用  rb  和 wb  的方式因为不知道要操作的文件时什么类型什么格式的
        path3 = os.path.join(path2, filename)
        if os.path.exists(path3):
            print('已有同名文件存在')
        with open(path1, 'rb')as f1, open(os.path.join(path2, filename), 'wb') as f2:
            # 直接将文件1中的内容读出来并写入到指定位置即可
            content = f1.read()
            f2.write(content)


# 成功啦!!!!!
copy(r'D:\FullStackD\Stack15\Day0603\Day07_01.py', r'D:\FullStackD\Stack15\Day0615')


# 3.获取某个文件所在目录的上一级目录
def upname(path):
    path1 = os.path.dirname(path)
    path2 = os.path.basename(path)
    return path, path1, path2


print(upname('D:\FullStackD\Stack15\Day0615'))

# 使用os模块创建如下目录结构
# 创建文件夹,创建文件
# os.makedirs('glance/api')
# os.makedirs('glance/cmd')
# os.makedirs('glance/db')
# open('glance/api/__init__.py','w').close()
# open('glance/api/policy.py','w').close()
# open('glance/api/versions.py','w').close()
# open('glance/cmd/__init__.py','w').close()
# open('glance/cmd/manage.py','w').close()
# open('glance/db/__init__.py','w').close()
# open('glance/db/model.py','w').close()

# 5.写一个用户注册登录的程序,每一个用户的注册都要把用户名和密码用字典的格式写入文件
# 在登录的时候,从文件中取出数据进行验证
import pickle


def register():
    usr = input('username:')
    pwd = input('password:')
    dic = {usr: pwd}
    with open('usrinfo', 'wb')as f:
        pickle.dump(dic, f)
    print("注册成功")


def login():
    Flag = True
    usr = input('username:')
    pwd = input('password:')
    with open('usrinfo', 'rb')as f:
        while Flag:
            try:
                dic = pickle.load(f)
                for k, v in dic.items():
                    if k == usr and v == pwd:
                        print("登陆成功")
                        Flag = False
                        break
            except EOFError:
                print('登录失败')
                break


# register()
# login()

# 发红包
import random


def bonus(money, num):
    # 将小数点去掉
    money = money * 100
    ret = random.sample(range(1, money), num-1)
    ret.sort()
    ret.insert(0, 0)
    ret.append(money)
    # 再把小数点去掉,形成实际红包数
    for i in range(len(ret) - 1):
        yield ((ret[i + 1] - ret[i]) / 100)
    return ret


# print(bonus(200, 9))
ret_g = bonus(200, 10)
print('123123123')
for money in ret_g:
    print(money)


# 抢红包的程序
def hongbao(sum, n):
    lst = []
    # 限制个数
    for i in range(n - 1):
        number = random.uniform(0, sum)
        number = round(number, 2) #保留两位小数
        # 每一次都将红包金额总数做处理
        sum = sum - number
        lst.append(number)
    lst.append(sum)
    random.shuffle(lst)
    return lst


lst = hongbao(50, 3)
print(lst)

