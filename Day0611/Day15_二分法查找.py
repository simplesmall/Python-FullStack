lst = [11, 22, 33, 44, 55, 66, 77, 88, 99]
n = 33
# for el in lst:
#     if el == n:
#         print("找到了")
#         break
# else:
#     print("没找到")

left = 0
right = len(lst) - 1
while left < right:
    mid = (left + right) // 2
    if lst[mid] > n:
        right = mid - 1
    if lst[mid] < n:
        left = mid + 1
    if lst[mid] == n:
        print("找到了")
        break
else:
    print("没有找到")

# 递归完成二分法
lst = [22, 33, 44, 55, 66, 67, 88, 90, 123, 125, 233]


def func(n, left, right):
    if (left <= right):
        mid = (left + right) // 2
        if n > lst[mid]:
            left = mid + 1
            return func(n, left, right)
        if n < lst[mid]:
            right = mid - 1
            return func(n, left, right)
        if n == lst[mid]:
            print("找到了")
            return mid
    else:
        print("没有这个数")
        return -1


ret =func(66 , 0, len(lst) - 1)
print(ret)
