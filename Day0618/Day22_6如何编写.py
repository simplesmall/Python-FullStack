#方式一 :归类+提取公共值  归类:反推
#方式二: 在指定类中编写和当前类相关的所有代码
class file_operater:
    def __init__(self,file_path):
        self.filepath = file_path
    def file_read(self):
        pass
    def file_update(self):
        pass
    def file_delete(self):
        pass
    def file_add(self):
        pass
class excel_operater:
    def excel_read(self): 
        pass
    def excel_update(self):
        pass
    def excel_delete(self):
        pass
    def excel_add(self):
        pass