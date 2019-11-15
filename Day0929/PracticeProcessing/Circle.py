radius = int(input("请输入圆的半径:"))
diam = radius * 2
perimeter = 2 * 3.14 * radius
facePerimeter = 4 * 3.14 * radius * radius
volume = 4 / 3 * 3.14 * radius * radius

print('圆的直径:' ,diam, '圆周长:%f' % perimeter, '圆表面积:%f' % facePerimeter, '圆体积:%.3f' % volume)
