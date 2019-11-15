#模块之间不允许循环引用
"""
import b
def  funca():
    print('Funcrion A)
b.funcb()
"""

"""
import a
def funcb():
    print('Function A)
a.funca()
"""