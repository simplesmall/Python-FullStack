"""
创建三个学校的设施内容是一致的
"""


class School(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def speech(self):
        print('讲课')


obj1 = School('北京校区', '沙河')
obj2 = School('上海校区', '浦东新区')
obj3 = School('深圳校区', '南山区')


class Teacher(object):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary
        self.school = None


t1 = Teacher('李姐', 19, 188888)
t2 = Teacher('严涛', 18, 879089)
t3 = Teacher('女神', 16, 6756756)

#     做到数据之间的嵌套
###########给老师分配校区
t1.school = obj1
t2.school = obj2
t3.school = obj3

########查看老师信息
print(t1.school.name,t1.school.address)
print(t2.name,t2.age)
t3.school.speech()