s = "123"
for i in s:
    print(i)
print(dir(str))
# print(str.__doc__)

lst = ["赵旖旎","史可心","张娜拉","孙中山"]

it = lst.__iter__()
while 1 :
    try:
        el = it.__next__()
        print(el)
    except  StopIteration:
        break
