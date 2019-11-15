from django.test import TestCase


# Create your tests here.
class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ":" + str(self.age)


alex = Animal("Alex", 23)
egon = Animal("Egon", 34)

print(alex)
print(egon)
