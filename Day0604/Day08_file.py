"""
1.文件操作的函数
    open(文件名(路径),mode = "?",encoding = "字符集")
2.模式: r,w,a,r+,w+,a+,rb,wb,ab,r+b,w+b,a+b
3.常用的操作
    1.光标(seek)
    2.tell
    3.truncate
"""

f = open("file.txt",mode="r",encoding="UTF-8")
s = f.read()
print(s)
f.close()#如果没有这句话则在后面删除这个文件时会报错

f  = open("axiba",mode="a",encoding="utf-8")
f.write("养狗了没有")
f.flush()
f.close()

#无论读取了多少内容,光标在哪,写入的时候都是在结尾写入,除非上来就写入,这时写入在开头
# 一定记得先读再写
#r+是读写同时存在的最好的模式
f = open("axiba",mode="r+",encoding="utf-8")
s= f.read()
print(s)
f.write("不养了,送人")
f.close()


# w+打开的所以写入之前先把文件里面的东西清除再写入
f = open("file.txt",mode="w+",encoding="utf-8")

f.write("There are something ...")
# 移动光标至句子开头,seek()
f.seek(0)
s = f.read() #写完之后直接读不会有好结果,因为光标在最后,取出的内容为空
print("取出的内容是:",s)
f.flush()
f.close()

f = open("file.txt",mode="a+",encoding="utf-8")
f.write("我是中文")
f.seek(0)
s = f.read()#不加seek移动光标读出来为空,因为a+的时候光标在最末尾
f.flush()
print("Content",s)
f.close()

f = open("axiba",mode="r",encoding="utf-8")
for line in f:
    print(line.strip())
f.close()
