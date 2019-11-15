from urllib import request
ret = request.urlopen('https://www.cnblogs.com/Eva-J/articles/7292109.html')
print(ret.read().decode('utf-8'))