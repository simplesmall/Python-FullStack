import queue
import threading
import time

q = queue.Queue()


def producer(id):
    while True:
        time.sleep(2)
        q.put('包子')
        print('厨师%s生产了一个包子' % id)


for i in range(1, 4):
    t = threading.Thread(target=producer, args=(i,))
    t.start()


def consumer(id):
    while True:
        time.sleep(1)
        v1 = q.get()
        print('抓鱼锅%s吃了一个包子' % id)


for i in range(1, 3):
    t = threading.Thread(target=consumer, args=(i,))
    t.start()
