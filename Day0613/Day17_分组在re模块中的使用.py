import  re
s = '<a>wahaha</a>'
ret = re.search('(>)(\w+)(<)',s)
print(ret.group())
print(ret.group(1))
print(ret.group(2))
print(ret.group(3))
s = re.search('<(\w+)>(\w+)</(\w+)>',s)
print(s.group(1))
print(s.group(2))
print(s.group(3))

#取消分组优先 ?:
ret = re.findall('\d+(?:\.\d+)?','1.234*4.3')
print(ret)

ret = re.split('(\d+)','alex12jian23xiao78')
print(ret)

#分组命名
s = '<a>wahahahaha</a>'
ret = re.search('>(?P<con>\w+)<',s)
print(ret.group(1))
print(ret.group('con'))