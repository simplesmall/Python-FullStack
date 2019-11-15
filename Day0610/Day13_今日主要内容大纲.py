n = 6
for i in range(1,n+1):
    for k in range(2*n - 2*i):
        print("",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()

lst = ["111","222","333","444"]
for el in lst:
    print(el)

for index,el in enumerate(lst):
    print(index,el)

dic = {"11":"aa","22":"bb","33":"cc"}
for k,v in dic.items():
    print(k,v)