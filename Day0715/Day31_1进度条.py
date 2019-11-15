import time
# print('\r80%',end='')
# time.sleep(2)
# print('\r90%')
#
# tpl = "进度条目前是%s%%"%(90,)
# print(tpl)

def func(size,totalsize):
    percent = int(size/totalsize *100)
    time.sleep(0.1)
    print('\r%s%%|%s'%(percent,"#"*percent),end='')

for i in range(101):
    func(i,100)
