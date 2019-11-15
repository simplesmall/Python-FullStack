from  arrays import Arrays
a = Arrays(5)
print(len(a))
print(a)

for i in range(len(a)):
    a[i]=i+1
print(a)