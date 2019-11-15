import hashlib

obj = hashlib.md5()
obj.update("hello".encode('utf-8'))
result = obj.hexdigest()
print(result)
# 5d41402abc4b2a76b9719d911017c592

##############   加盐
obj = hashlib.md5(b'jiayan')
obj.update("hello".encode('utf-8'))
result = obj.hexdigest()
print(result)
#  686a12bb5577133d6698131cbf0b4b4a

def md5(pwd):
    obj = hashlib.md5(b'jiayan')
    obj.update(pwd.encode('utf-8'))
    return obj.hexdigest()
print(md5('hello world'))

user = input('请输入姓名:')
pwd = input('请输入密码:')
if user == 'oldboy' and md5(pwd) == '686a12bb5577133d6698131cbf0b4b4a':
    print('登录成功')
else:
    print('用户名或密码错误')