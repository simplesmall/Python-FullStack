import threading
import time

def task():
    time.sleep(2)
    print("拿快递")
#创建一个线程
t = threading.Thread(target=task)

t.start()

print("开始自嗨")
print("喝瓶老白干")
print("擦擦嘴")