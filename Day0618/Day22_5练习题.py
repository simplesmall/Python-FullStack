class UserInfo:
    def __init__(self):
        self.name=None
    def info(self):
        print('当前用户名称:%s'%(self.name,))
    def account(self):
        print('当前用户%s的账单是...'%(self.name,))
    def shopping(self):
        print('%s购买了一个人形抱枕'%(self.name,))
    def login(self):
        user = input('User name please:')
        pwd = input('Password please:')
        if pwd =='sb':
            self.name == user
            while True:
                print("""
                1.查看用户信息
                2.查看用户账单
                3.购买抱枕
                """)
                num = int(input('Enter your choose please:'))
                if num ==1:
                    #此处等价于obj.info
                    self.info()
                elif num == 2:
                    self.account()
                elif num == 3:
                    self.shopping()
        else:
            print('Login Error')
obj = UserInfo()
obj.login()