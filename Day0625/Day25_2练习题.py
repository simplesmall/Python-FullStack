class StarkConfig(object):
    list_display = []

    def get_list_display(self):
        self.list_display.insert(0, 33)
        return self.list_display


class RoleConfig(StarkConfig):
    list_display = [11,22]

#####第一题
s1 = StarkConfig()
result1 = s1.get_list_display()
print(result1)

result2 = s1.get_list_display()
print(result2)

#####第二题
s2 = StarkConfig()
result1 = s1.get_list_display()
print(result1)

result2 = s1.get_list_display()
print(result2)

#####第三题
s3 = StarkConfig()
s4 = RoleConfig()
result3 = s3.get_list_display()
result4 = s4.get_list_display()
print(result3)
print(result4)

#####第四题
s5 = RoleConfig()
s6 = RoleConfig()
result5 = s5.get_list_display()
result6 = s6.get_list_display()
print(result5)
print(result6)
