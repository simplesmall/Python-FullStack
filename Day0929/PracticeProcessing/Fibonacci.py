def fib(n):
    if n<3:
        return 1
    else:
        return fib(n-1)+fib(n-2)

# ret = fib(4)
# print(ret)

def fibo(n,counter):
    sum=1
    first=1
    second=1
    count=3
    while count<n:
        counter+=1
        sum=second+first
        first=second
        second=sum
        count+=1
    return sum
ret=fibo(8,0)
print(ret)
