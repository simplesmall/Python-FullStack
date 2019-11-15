from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
from app01.models import User,Role
def login(request):
    if request.method=="POST":
        # 认证
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")
        user = User.objects.filter(name=user,pwd=pwd).first()
        if user:
            # 登录成功
            # 保存登录信息
            request.session["user_id"]=user.pk
            # 查询当前登录人的所有权限列表  下面两种写法是一样的
            # ret = user.roles.all()
            # 返回的是 角色表
            role=Role.objects.filter(user=user)
            print("Roles------>",role)
            # 通过角色正向查询权限表,直接在values()里面调用__加字段的方式
            permissions=Role.objects.filter(user=user).values("permissions__url").distinct()
            print("Permission----->",permissions)
            permissions_list=[]
            for item in permissions:
                permissions_list.append(item["permissions_url"])

            # 将当前登录人的权限列表注入session中
            request.session["permission_list"]=permissions_list
            return  HttpResponse("登录成功")
    return render(request,"login.html")

def customers(request):
    if request.method == "POST":
        #  添加
        return HttpResponse("添加成功")

    # 查看
    return HttpResponse("customers")


def orders(request):
    return HttpResponse("orders...")


def addorders(request):
    return HttpResponse("addorders...")


def eidtorders(request,id):
    return HttpResponse("eidtorders...")

def deleteorders(request,id):
    return HttpResponse("deleteorders...")

def addcustomers(request):
    return HttpResponse("addcustomers...")

def editcustomers(request,id):
    return HttpResponse("addcustomers...")

def deletecustomers(request,id):
    return HttpResponse("deletecustomers")