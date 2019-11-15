import threading
import multiprocessing
import time

lock = threading.RLock()

def task(arg):
    print('抓鱼锅来了')
    lock.acquire()
    time.sleep(2)
    print(arg)
    lock.release()

if __name__ == '__main__':
    p1 = threading.Thread(target=task,args=(1,))
    p1.start

    p2 = multiprocessing.Process(target=task, args=(2,))
    p2.start