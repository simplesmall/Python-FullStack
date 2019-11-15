a = 9
print(a//3)

# print('a'+'b'+1)
print(range(3))

print('abcd'.replace('ab','cd'))
print(1 >2 and  3 or 6)

dic = {}
s = "name:apple|price:100|amount:3|year:2019"
lst = s.split("|")
for el in lst:
    ll=el.split(":")
    dic[ll[0]]=ll[1]
print(dic)