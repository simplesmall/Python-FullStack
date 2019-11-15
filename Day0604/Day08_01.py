print("y6tdfy")
"""
seek(0,0)开头位置
seek(0,1)当前位置
seek(0,2)末尾位置

"""
f=open("axiba",mode="r",encoding="utf-8")
f.seek(3)
s = f.read(1)
print(f.tell())
f.close()

# truncate删除光标后面所有内容
f=open("axiba",mode="w",encoding="utf-8")
f.write("哇哈哈哈猪")
f.seek(9)
print(f.tell())
# 默认是截取到光标位置,加了参数之后截断到参数位置
f.truncate(15)
f.flush()
f.close()

