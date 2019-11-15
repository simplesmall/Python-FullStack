# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(100))

L = ['Michael','Sarah','Tracy']
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
print(L[:3])
print(L[1:2])
# 生成一个从0 - 99的随机数组
L = list(range(10))
print(L)
# 前面几项,每隔两个输出
print(L[:6:2])
# 如下所示就可以完全复制一个数组
print(L[:])
# tuple切片操作
print((1,2,3,4,5,"123",234)[:])

for key in L:
    # print(key)
    pass

for i,value in enumerate(['a,','b','c']):
    print(i,value)

for x,y in [(1,2),(2,4),(3,6)]:
    print(x,y)

it = iter([2,3,5,4,7])
print(next(it))
print(next(it))
print(next(it))

print([x*x for x in range(1,11)])
print([x*x*x for x in range(1,10) if x%2 ==0])
print([m+n for m in 'ABC' for n in 'XYZ'])

