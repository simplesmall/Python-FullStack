"""
1.基本数据类型 int bool str list  turple  dict  set

2.bit_length()返回二进制长度
3.bool 类型
  类型转换:用目标数据类型括起来就可以
  当成False:所有的空都是False,非空都是True
4.str字符串(String)
    1.索引和切片,对象是列表.split()是切割,对象是字符串
        索引下标从0开始,[索引]
        切片:[起始位置:终止位置:步长]
            1.顾头不顾尾
            2.默认从左往右取
            3.步长为负数,从右往左取,调整对应的起始终止位置.
    2.常用操作:
        1.upper(),  变成大写字母
        2.strip(),   去掉左右两边空格
        3.replace(), 替换
        4.split(),   切割
        5.startswith(),是否以XXX开头
        6.len(),     长度,内置函数
        7.count(),find(),index() 计数  是否有  返回位置
    3.迭代
        for 变量 in 可迭代对象:
            循环体
        表示把可迭代对象中的每一个元素赋值给前面的变量
        //像 dict set 之类没有标号的数据类型没有标号不能被用于查所以用while不能完成可迭代对象的所有操作
        //故而所有统一采用for循环

"""
name = 'alex leNb'
print(name.strip('a').strip('b'))
print(name.startswith('al'))
print(name.endswith('nb'))
print(name.replace('l','P'))
print(name.split('l'))
# print(name.split('l',1))
print(name.upper())
print(name.lower())
print(name.count('l'))
print(name.count('l',0,4))
print(name.index('N'))
print(name.find('lex'))
print(name[2])        #e
print(name[:3])       #ale
print(name[-1:-3:-1]) # bN
print(name[-2:])      # Nb
index = 0 #手动记录索引位置
for c in name:
    if c == 'e':
        print(index)
    index+=1

s = '123a4b5c'
print(s[:3])
print(s[::2])
print(s[-3::-2])

s = "asdwer"
for c in s:
    print(c+'sb')

s = '321'
for c in s:
    print(c+"秒倒计时")
else:
    print("出发")

# shizi = input("请输入计算式子")
# shizi = shizi.replace(" ","")
# lst = shizi.split("+")
# print(int(lst[0])+int(lst[1]))

count = 1
sum = 0
while count <= 99:
    if count ==88:
        count+=1
        continue
    if count %2 ==0:
        sum -=count
    else:
        sum+=count
    count +=1
print(sum)

# content = input("请输入一句话:")
# daxie = 0
# xiaoxie = 0
# shuzi = 0
# other = 0
# for c in content:
#     if c.isupper():
#         daxie+=1
#     elif c.islower():
#         xiaoxie+=1
#     elif c.isdigit():
#         shuzi+=1
#     else:
#         other+=1
# print(daxie,xiaoxie,shuzi,other)

first_names = """
赵钱孙李，周吴郑王。
冯陈褚卫，蒋沈韩杨。
朱秦尤许，何吕施张。
孔曹严华，金魏陶姜。
戚谢邹喻，柏水窦章。
云苏潘葛，奚范彭郎。
鲁韦昌马，苗凤花方。
俞任袁柳，酆鲍史唐。
费廉岑薛，雷贺倪汤。
滕殷罗毕，郝邬安常。
乐于时傅，皮卞齐康。
伍余元卜，顾孟平黄。
和穆萧尹，姚邵湛汪。
祁毛禹狄，米贝明臧。
计伏成戴，谈宋茅庞。
熊纪舒屈，项祝董梁。
杜阮蓝闵，席季麻强。
贾路娄危，江童颜郭。
梅盛林刁，钟徐邱骆。
高夏蔡田，樊胡凌霍。
虞万支柯，昝管卢莫。
经房裘缪，干解应宗。
丁宣贲邓，郁单杭洪。
包诸左石，崔吉钮龚。
程嵇邢滑，裴陆荣翁。
荀羊於惠，甄曲家封。
芮羿储靳，汲邴糜松。
井段富巫，乌焦巴弓。
牧隗山谷，车侯宓蓬。
全郗班仰，秋仲伊宫。
宁仇栾暴，甘钭厉戎。
祖武符刘，景詹束龙。
叶幸司韶，郜黎蓟薄。
印宿白怀，蒲邰从鄂。
索咸籍赖，卓蔺屠蒙。
池乔阴鬱，胥能苍双。
闻莘党翟，谭贡劳逄。
姬申扶堵，冉宰郦雍。
卻璩桑桂，濮牛寿通。
边扈燕冀，郏浦尚农。
温别庄晏，柴瞿阎充。
慕连茹习，宦艾鱼容。
向古易慎，戈廖庾终。
暨居衡步，都耿满弘。
匡国文寇，广禄阙东。
欧殳沃利，蔚越夔隆。
师巩厍聂，晁勾敖融。
冷訾辛阚，那简饶空。
曾毋沙乜，养鞠须丰。
巢关蒯相，查后荆红。
游竺权逯，盖益桓公。
万俟司马，上官欧阳。
夏侯诸葛，闻人东方。
赫连皇甫，尉迟公羊。
澹台公冶，宗政濮阳。
淳于单于，太叔申屠。
公孙仲孙，轩辕令狐。
钟离宇文，长孙慕容。
鲜于闾丘，司徒司空。
丌官司寇，仉督子车。
颛孙端木，巫马公西。
漆雕乐正，壤驷公良。
拓跋夹谷，宰父谷梁。
晋楚闫法，汝鄢涂钦。
段干百里，东郭南门。
呼延归海，羊舌微生。
岳帅缑亢，况郈有琴。
梁丘左丘，东门西门。
商牟佘佴，伯赏南宫。
墨哈谯笪，年爱阳佟。
第五言福，百家姓终。
"""
name = input("输入你的名字:")
sum = ''
for c in name:
    sum +=c
    if sum in first_names:
        print("在百家姓中")
        break
else:
    print("不在百家姓中")