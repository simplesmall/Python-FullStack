class Foo:
    def __init__(self):
        pass

    def __display(self):
        print('6666')
        return '__display return'
        print('88888')

    def another(self):
        print(self.__display())
        return 'another return'


obj = Foo()
ret = obj.another()
print(ret)
