import threading

############1.计算密集型任务,多线程无法提高运行速度#######################
# v1 = [11, 22, 33]
# v2 = [44, 55, 66]
#
# def func(data,plus):
#     for i in range(len(data)):
#         data[i] +=plus
#
# t1 = threading.Thread(target=func,args=(v1,1))
# t1.start()
#
# t2 = threading.Thread(target=func,args=(v2,100))
# t2.start()
#
# print(v1)
# print(v2)

import requests
import uuid

url_list=[
    'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1297505592,1789076279&fm=27&gp=0.jpg',
    'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1638079650,2146947483&fm=27&gp=0.jpg',
    'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3925233323,1705701801&fm=27&gp=0.jpg'
]

def task(url):
    ret = requests.get(url)
    file_name = str(uuid.uuid4())+'.jpg'
    with open(file_name,'wb') as f:
        f.write(ret.content)
for url in url_list:
    t = threading.Thread(target=task,args=(url,))
    t.start()

