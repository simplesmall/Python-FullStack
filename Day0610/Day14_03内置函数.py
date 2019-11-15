lst = ["白蛇传","仙剑三","琅琊榜"]
its = lst.__iter__()
print(its.__next__())
it = iter(lst)
print(it.__next__())
print(next(it))

