import threading
import time

def task(n):
    time.sleep(5)

    print("开始执行任务:",n)
    print(".........")
    print("任务完毕\n")

while True:
    name = input("请输入任务:")
    t = threading.Thread(target=task,args=(name,))
    t.start()