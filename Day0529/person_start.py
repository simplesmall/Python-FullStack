class Person:
    def __init__(self,name,age,pay=0,job=None):
        self.name=name
        self.age=age
        self.pay=pay
        self.job=job
    def lastName(self):
        return self.name.split()[-1]
if __name__ =='__main__':
    bob = Person('Bob Smith',42,30000,'software')
    smith = Person('Bill Smith',48,50000,'hardware')
    print(bob.name,smith.pay)
    print(bob.lastName())
    print(Person)

people = [bob,smith]
for person in people:
    print(person.name,person.pay)
print([(person.name,person.job) for  person in people])

print([rec.name for rec in people if rec.age>40])
print([(rec.age ** 2 if  rec.age>45 else rec.age) for rec in people if rec.age>40])
