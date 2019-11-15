print(repr("就是这样的\iugcasd"))
s = "5+6"
ret = eval(s)
print(ret)

s = "for i in range(10): print(i)"
c = compile(s,"","exec")
exec(c)

s = "content = input('请输入名字:')"
c = compile(s,"","single")
exec(c)
print(content)