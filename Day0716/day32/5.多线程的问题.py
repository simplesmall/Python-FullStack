import threading
import time

lock = threading.RLock()

n = 10

def task(i):
    print('这段代码不加锁',i)

    lock.acquire() #加锁
    global n
    print('当前线程:', i, '读取到的n值为:', n)
    n = i
    time.sleep(1)
    print('当前线程:', i, '修改后的n值为:', n, "\n")
    lock.release()  #释放锁

for i in range(10):
    t = threading.Thread(target=task, args=(i,))
    t.start()
