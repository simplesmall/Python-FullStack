# import threading
# import time
#
# print('start')
#
#
# ##############1.线程的基本使用############
# def func(arg):
#     time.sleep(2)
#     with open('a.py','wb') as f:
#         f.write(b'111')
#
#
# t1 = threading.Thread(target=func, args=(1,))
# t1.start()
#
# t2 = threading.Thread(target=func, args=(2,))
# t2.setDaemon(True)  # 设置为主线程不再等待子线程执行
# t2.start()
# #############2.主线程默认等待子线程执行完毕###
# print('end')
#

###############4.开发者可以控制主线程等待子线程(最多等待时间)##########
# import time
# import threading
# def func(arg):
#     time.sleep(3)
#     print(arg)
#
# print('创建子线程1')
# t1 = threading.Thread(target=func,args=(2,))
# t1.start()
# t1.join(4)  #让主线程等待直到子线程完毕才继续往下走,里面的参数为等待时间,无参数则等待直到子线程结束
#
# print('创建子线程2')
# t2 = threading.Thread(target=func,args=(4,))
# t2.start()
# t2.join(2)
# print(123)

###################################4.线程名称#########################
# import time
# import threading
# def func(arg):
#     #获取当前执行该函数的线程的对象
#     t = threading.current_thread()
#     #根据当前线程对象获取当前线程名称
#     name = t.getName()
#     print(name,arg)
#
# t1 = threading.Thread(target=func,args=(11,))
# t1.setName('First threading')
# t1.start()
#
# t2 = threading.Thread(target=func,args=(22,))
# t2.setName('抓鱼锅')
# t2.start()
#
# print(123)


########################################5.线程本质###############
# import threading
# def func(arg):
#     print(arg)
#
# t1 = threading.Thread(target=func,args=(11,))
# t1.start()
# # start 告诉CPU,一切准备就绪,可以调度我了
# print(123)

#####################################6.补充:面向对象版本的多线程#######
import threading
def func(arg):
    print(arg)

t1 = threading.Thread(target=func,args=(11,))
t1.start()

class MyThread(threading.Thread):
    pass

t1 = MyThread(target=func,args=(11,))
t1.start()