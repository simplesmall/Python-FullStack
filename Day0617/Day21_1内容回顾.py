print("内容回顾")
try:
    pass
except EOFError:
    print('1')
except NameError:
    print('2')
except Exception as e:
    print(e)
except (Ellipsis,NotADirectoryError):
    print('综合错误,比如提示:这些错误都是由于.....')
else:
    print('else')
finally: #例如打开文件,文件不存在,我们都知道要报错,但是要先关闭文件,然后报错退出
    print('Finally output')

# raise ValueError

assert 1==1
print('assert successful')