from core import search
def home():
    print('欢迎来到员工信息查询中心')
    operate_lst = ['查询','修改','删除','添加']
    for index,item in enumerate(operate_lst,1):
        print(index,item)
    num = int(input('请输入要执行的操作:'))
    if num == 1:
        search.select()
    elif num ==2:
        print('修改')
    elif num == 3:
        print('删除')
    elif num == 4 :
        print('添加')
    else:
        print('不支持的操作')
