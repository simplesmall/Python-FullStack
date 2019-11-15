class Pagenation():
    """
        处理分页相关的代码
    """

    def __init__(self, page_list, page, per_page_num=10):
        """
        初始化,page为第几页,per_page_num为默认每页多少条数据
        :param page:
        :param per_page_num:
        """
        self.page_list = page_list
        self.page = page
        self.per_page_num = per_page_num

    @property
    def start(self):
        """
        计算索引的起始位置
        :return:
        """
        return (self.page - 1) * self.per_page_num

    @property
    def end(self):
        """
        计算索引的结束位置
        :return:
        """
        return self.page * self.per_page_num

    def show(self, page_list):
        page_data_list = page_list[obj.start:obj.end]
        for item in page_data_list:
            print(item)


page_list = []
for i in range(1, 301):
    page_list.append('name = %s' % i)
while True:
    page = int(input('Please input page what you want:'))

    # per_page_num = 10
    #
    # start = (page - 1) * per_page_num
    # end = page * per_page_num

    obj = Pagenation(page_list, page)
    # 为了避免在调用中省去()括号的使用,将其设置为@property类型就可以
    obj.show(page_list)
