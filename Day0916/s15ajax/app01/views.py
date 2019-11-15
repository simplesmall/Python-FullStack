from django.shortcuts import render,HttpResponse

# Create your views here.

from app01.models import UserInfo
import json

def index(request):


    return render(request,"index.html")



def handle_ajax(request):

    return HttpResponse("Yuan")


def cal(request):
    import time

    # time.sleep(10)
    # print(request.GET)
    # num1=request.GET.get("num1")
    # num2=request.GET.get("num2")
    num1=request.POST.get("num1")
    num2=request.POST.get("num2")
    ret=int(num1)+int(num2)
    return HttpResponse(str(ret))



def login(reqeust):

    if reqeust.method=="POST":

        res={"user":None,"error":""}

        print(reqeust.POST)
        user=reqeust.POST.get("user")
        pwd=reqeust.POST.get("pwd")

        user_obj=UserInfo.objects.filter(user=user,pwd=pwd).first()
        if user_obj:
            res["user"]=user
        else:
            res["error"]="用户名或者密码错误！"
        return HttpResponse(json.dumps(res))

    else:
        return render(reqeust,"login.html")

def name(request):
    print(request.POST)
    return  HttpResponse("OK")

def file_put(request):

    print(request.POST)
    print(request.FILES)
    file_obj=request.FILES.get("file_obj")
    # print(file_obj.name)
    path=file_obj.name
    with open(path,"wb") as f:
        for line in file_obj:
            f.write(line)
    return  HttpResponse("OK")