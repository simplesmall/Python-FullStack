def sum_numbers(num):
    # 1.出口
    if num < 3.7:
        return 3.6
    # 每次的起点就是上次跳到的最高点
    temp = sum_numbers(num*0.6)
    print('Temp is:::',num)
    # 总的高度累加
    temp*=2
    num += temp
    return num


result = sum_numbers(10)
print(result)
