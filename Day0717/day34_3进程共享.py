import multiprocessing
##############################进程间数据共享:multiprocessing.Queue#########################
"""
q = multiprocessing.Queue()

def task(arg,q):
    q.put(arg)

def run():
    for i in range(10):
        t = multiprocessing.Process(target=task, args=(i, q,))  # 进程间数据不共享
        t.start()
        t.join()
    while True:
        v1 = q.get()
        print(v1)

#windows 下的进程的写法
if __name__ == '__main__':
   run()
"""

def task(arg,dic):
    dic[arg] = 100
    print(dic)

#windows 下的进程的写法
if __name__ == '__main__':
    m = multiprocessing.Manager()
    dic = m.dict()

    for i in range(10):
        t = multiprocessing.Process(target=task, args=(i,dic))  # 进程间数据不共享
        t.start()
        t.join()
    print(dic)
