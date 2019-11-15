from django.shortcuts import render,HttpResponse

# Create your views here.

import datetime
def timer(request):
    # return HttpResponse("Guan 123")

    now = datetime.datetime.now().strftime("%Y-%m-%d")

    return HttpResponse(now)

def login(request):
    return render(request,"login.html")

def auth(request):
    print(request.POST)  #{'user': ['alex'], 'pwd': ['123']}
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    print(user,pwd)
    return  HttpResponse("OK")

