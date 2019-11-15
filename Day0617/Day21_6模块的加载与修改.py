import time
import importlib
import my_module

time.sleep(2)
#重新加载修改过的模块
importlib.reload(my_module)
my_module.red1()