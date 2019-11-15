"""
regex
查找
findall
search
match
z字符串处理的扩展:替换,切割
split
sub
subn

re模块的进阶
compile  节省使用正则表达式解决问题的时间
finditer  节省使用正则表达式解决问题的空间
"""
import re

# findall匹配所有
ret = re.findall('\d+', 'asdkbk213kjb134')
print(ret)

# search 只匹配从左到右第一个
ret = re.search('\d+', 'asdjk123kj5412')  #
print(ret)  # 内存地址,这是一个职责匹配的结果
print(ret.group())  # 获取真正的结果
ret = re.search('\d+', 'gdgha23')
if ret:
    print(ret.group())

# match 从开始的位置开始寻找
ret = re.match('\d+', '23jjaagts123ajs143')
# 等效于 ret = re.search('^\d+','jjaagts123ajs143')
print(ret)

s = 'alec23jiayubn78dhb12'
ret = re.split('\d+',s)
print(ret)

#sub 谁  旧的  新的  替换次数
ret = re.sub('\d+','H','alex12jiushi23bjsd22')
print(ret)
ret = re.sub('\d+','H','alex12jiushi23bjsd22',1)
print(ret)
#subn  返回一个元组,第二个元素是替换的次数
ret = re.subn('\d+','H','alex12jiushi23bjsd22')
print(ret)

#compile 将正则表达式编译成字节码,一次编译到处可用
ret = re.compile('\d+')
print(ret)
res = ret.findall('javsjhv2w4kjba56787868uhjva2367')
print(res)
ren = ret.findall('jbadbjk678a354gh546')
print(ren)

ret = re.finditer('\d+','alex234sav2343gvjhvxcgvjhcs23xjhvcvsd2334')
print(ret)
for i in ret:
    print(i.group())