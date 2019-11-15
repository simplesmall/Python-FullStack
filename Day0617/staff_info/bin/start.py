import sys
import os
# print(sys.path)
#获取start.py的路径
#当前文件往上翻两层 staff_info
project_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_path) #把staff_info添加到sys.path中
print(project_path)

from core import main
if __name__ == '__main__':
    main.home()

