from django.shortcuts import render,HttpResponse

# Create your views here.
from django.views import View


class LoginView(View):
    # 这样一来效果跟直接使用父类的dispatch一样的,不同之处仅仅在于在此处是类中所有操作都要经过的
    # 必须流程,可以在此处加设公共处理部分
    def dispatch(self, request, *args, **kwargs):
        print("DISPATCH....")
        ret=super().dispatch(request,*args,**kwargs)
        return ret
    def get(self,request):
        print("GET....")
        return render(request,"login.html")

    def post(self,request):
        print("POST.....")
        return HttpResponse("OK")