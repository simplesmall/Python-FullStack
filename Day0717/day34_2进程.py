import multiprocessing
import threading

data_list = []

def func(arg):
    p = multiprocessing.current_process()
    print(p.ident,p.pid)
    data_list.append(arg)
    print(data_list)
def run():
    for i in range(10):
        t = multiprocessing.Process(target=func,args=(i,))  #进程间数据不共享
        # t = threading.Thread(target=func,args=(i,))  #线程下面逐一增多,全局记录数据累加
        t.start()
        t.join()

#windows 下的进程的写法
if __name__ == '__main__':
    run()


##########################################通过继承方式创建进程###################
class MyProcess(multiprocessing.Process):
    def run(self):
        print('当前进程',multiprocessing.current_process())

def run():
    p1 = MyProcess()
    p1.start()

    p2 = MyProcess()
    p2.start()

if __name__ == '__main__':
    run()