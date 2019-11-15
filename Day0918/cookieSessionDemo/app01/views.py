from django.http import HttpResponse
from django.shortcuts import render, redirect

from app01.models import UserInfo


# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        print(user, pwd)
        user_obj = UserInfo.objects.filter(user=user, pwd=pwd).first()
        # 此处的关键在于
        '''
        login  response 请求时是服务器返回cookie
        index  request 请求时带着cookie去的
        '''
        if user_obj:
            obj = redirect('/index/')
            #  设置cookie
            obj.set_cookie("username", user)
            obj.set_cookie("is_login", True)  # max_age=20  20秒后cookie被清除
            return obj
        else:
            return HttpResponse('fail')


def index(request):
    # 获取cookie
    print(request.COOKIES)

    is_login = request.COOKIES.get('is_login')
    if not is_login:
        return redirect('/login/')

    name = request.COOKIES.get("username")
    shangpin = ['香蕉', '苹果', '橘子']
    return render(request, 'index.html', {"name": name, "shangpin": shangpin})


# 无论用到还是没用到,只要在这一网站生成的cookie请求时都会带着走
def timer(request):
    import datetime
    return HttpResponse(str(datetime.datetime.now()))


def login_session(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        print(user, pwd)
        user_obj = UserInfo.objects.filter(user=user, pwd=pwd).first()
        # 此处的关键在于
        '''
        login  response 请求时是服务器返回cookie
        index  request 请求时带着cookie去的
        '''
        if user_obj:
            # 用户认证信息存储
            request.session["susername"] = user
            request.session["slogin"] = True
            '''
            if request.COOKIE.get("sessionid"):
                random_str = request.COOKIE.get("sessionod")
                在diango-session表中过滤session-key=random_str 的记录进行update
                    
            else:
            
            1 生成一个随机字符串   347jhsdv6y3vjhdfuyf
            2 向django-session 表中插入记录
                   session-key        session-data
                347jhsdv6y3vjhdfuyf  {"susername":"alex","slogin":True}
            3 响应set_cookie: {"sessionid":347jhsdv6y3vjhdfuyf}
            
            '''

            return redirect('/index_session/')
        else:
            return HttpResponse('fail')


def index_session(request):
    '''
    request.session
        1 request.COOKIE.get("sessionid")   : 347jhsdv6y3vjhdfuyf
        2 在django-session 表中过滤  session-key = 347jhsdv6y3vjhdfuyf的记录
        3 取过滤记录的session-data反序列化成字典 : {"susernaem":"alex","slogin":True}

        request.session相当于是将session-data中的数据饭序列化成字典格式的数据,然后在request.session.get
        中取出需要的数据项就可以直接用来判断和使用
    '''
    #  根据以上分析,此处取得session-date 中的 slogin = True ,然后再判断中条件为True
    slogin = request.session.get("slogin")

    if not slogin:
        return redirect('/login_session/')
    susername = request.session.get('susername')

    shangpin = ['香蕉', '苹果', '橘子']
    return render(request, 'index.html', {"name": susername, "shangpin": shangpin})


def logout(request):
    '''
    1 reuqest.COOKIE.get("sessionid") : 347jhsdv6y3vjhdfuyf
    2 在django-session 表中过滤 session-key=347jhsdv6y3vjhdfuyf的记录并删除
    3 response.delete_cookie(""sessionid)
    '''
    request.session.flush()
    return redirect("/login_session/")
