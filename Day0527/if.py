import  os
count = 1
while count<5:
    print(count)
    count+=1

# 让用户一直输入内容并打印,直到输入q的时候退出
flag = True
# while flag:
#     content = input('一直输入,按q退出')
#     if (content == 'q'):
#         flag = False
#     print(content)
"""
continue 与 break的区别:break 是彻底的停止掉当前层循环,continue停止当前本次循环,继续执行下一次循环
"""
name = "alex"
age = 38
hobby = "浪"
location = "湖边"
print(str(age) + "岁的"+name+"在"+location+"喜欢"+hobby)

print("%d岁的%s在%s喜欢%s"%(age,name,location,hobby))

print(1<2 and 2>3)
print(1<2 or 2>3)
print(not 1<2 or 2>3)

print(3 or 0)
print(2 and 1)
print(1 and 2)
print(0 or 1)
print('\n')
print(1 and 2 or 3)
print(1 or 2 and 3)
print(1>2 or 0 and 3<6 or 5)

print([d for d in os.listdir('.')])

