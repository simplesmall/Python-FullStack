from django.test import TestCase

# Create your tests here.

import json

# 轻量级的数据交换格式
l=[123,345,6578]
d={"name":"alex",'age':123}


s=json.dumps(d)
print(s) # {"name": "alex", "age": 123}



