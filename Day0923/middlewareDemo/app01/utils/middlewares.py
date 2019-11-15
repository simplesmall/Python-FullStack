from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect

'''
    中间件,最重要的意义在于所有经过这里的请求都必须走过所有的中间件
'''

# class PrintIPMiddleWare(MiddlewareMixin):
#     def process_request(self,request):
#         print(request.META.get("REMOTE_ADDR"))

class M1(MiddlewareMixin):
    def process_request(self,request):
        print("M1 request")
        #  中间件中如果在第一层就有返回的话就直接返回,不继续往下走
        # return HttpResponse("禁止")
    def process_response(self,request,response):
        print("M1 response")
        # 在此处更改response内容将会把之前过程中传输过来的内容自主替换掉
        return HttpResponse("我来试试")
    def process_view(self,request,callback,callback_args,callback_kwargs):
        print("M1 process_view...")
class M2(MiddlewareMixin):
    def process_request(self,request):
        print("M2 request")

    #    如果在此处写Response则有如下几种效果:
    #       如果后面的Request 不复写 response并且M1中的response不复写则会返回此处赋值的response
    #       如果M1的resquect复写了response则此处的赋值无效,将被覆盖掉

    def process_response(self,request,response):
        print("M2 response")
        # print(str(response))  # 要知道此处返回的response就是视图函数

        # 下面所示方法推演过程: return HttpResponse 中的HttpResponse中有关键方法content 就是直接读取返回的字符串的方法,
        # 所以调用type(resoponse)发现response的类型HttpResponse
        print("response",response.content)  # b'INDEX'
        return response

    #  在两者都正常执行下去的情况下的执行顺序是request1  request2  视图函数  response2  response1 结束
    def process_view(self,request,callback,callback_args,callback_kwargs):
        print("M2 process_view...")

class Login(MiddlewareMixin):
    def process_request(self,request):
        print(request.path)
        # 这是一种作为全局校验的检测是否登陆的办法
        if request.path in ["/login/"]:
            print("Login Middleware")
            # 这就是最关键的跳过中间件的代码
            # return None
        else:
            print("Login Middleware else part")
        # 作为校验检测是否登录,如果未登录的话则跳转至登录页面
        # if not request.user.is_authenticated:
        #     return redirect("/login/")