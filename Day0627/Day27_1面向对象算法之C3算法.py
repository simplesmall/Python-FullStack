print('C3算法')
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def message(self):
        return "全栈15期:%s,年龄: %s"%(self.name,self.age)

users = [Person('小明',23),Person('大张伟',21),Person('范晓晓',18)]

for item in users:
    # temp = "全栈15期:%s,年龄: %s"%(item['name'],item['age'])
    print(item.message())
