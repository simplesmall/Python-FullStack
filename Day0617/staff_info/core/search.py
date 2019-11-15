'''
查询相关的逻辑实现
'''
from conf import settings
def select():
    print('执行了select函数')
    # num = input('>>>')
    staff_info = settings.staffinfo
    print(staff_info)
    with open(staff_info) as f:
        for line in f:
            print(line.strip())