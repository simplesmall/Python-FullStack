import os
from django.core.exceptions import ValidationError

from django.shortcuts import render,HttpResponse

# Create your views here.
from  django import forms
# class BookForm(forms.Form):
#     title=forms.CharField(max_length=32)
#     price=forms.IntegerField()
#     email=forms.EmailField()

'''
    注册用户校验示例:
      用户名长度不能低于5位
      密码必须是纯数字
      邮箱必须符合邮箱格式
      如果输入数据格式有问题,显示给用户
'''
from django.forms import widgets

class UserForm(forms.Form):
    '''
    定义的要校验的字段必须与前端传过来的要校验的字段名称一致
    '''
    msg={"required":"该字段不能为空"}
    user=forms.CharField(min_length=5,
                         label="用户名",
                         error_messages=msg,
                         # 通过下面这一行设置将input加上class=form-control 的属性
                         widget=widgets.TextInput(attrs={"class":"form-control"})
                         )
    pwd=forms.CharField(
        label="密码",
        widget=widgets.PasswordInput(attrs={"class":"form-control"}))
    r_pwd = forms.CharField(
        label="确认密码",
        widget=widgets.PasswordInput(attrs={"class": "form-control"}))
    email=forms.EmailField(
        label="Email",
        widget=widgets.EmailInput(attrs={"class":"form-control"}))

    def clean_user(self):
        val= self.cleaned_data.get("user")
        ret=UserInfo.objects.filter(user=val).first()
        if not ret:
            return val
        else:
            raise ValidationError("用户名已存在")
    def clean_pwd(self):
        val= self.cleaned_data.get("pwd")
        if val.isdigit():
            raise ValidationError("密码不能是纯数字")
        else:
            return val
    def clean(self):
        pwd=self.cleaned_data.get("pwd")
        r_pwd=self.cleaned_data.get("r_pwd")
        if pwd and r_pwd:
            if pwd==r_pwd:
                return self.cleaned_data
            else:
                raise ValidationError("两个输入的密码不一致")
        else:
            return self.cleaned_data


from app01.models import UserInfo
def reg(request):
    if request.method=='POST':
        print(request.POST)

        # 数据校验
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            UserInfo.objects.create(**form.cleaned_data)
            return HttpResponse("Insert successful")
        else:
            print(form.errors)
        #     {"user":["","",""]} 字典里面的列表 Dict  List
        #  取值时以如下方式 form.errors.get("user")[0]


            errors = form.errors
            print('All errors:',form.errors.get("__all__"))
            if form.errors.get("__all__"):
                g_error=form.errors.get("__all__")[0]
            return render(request,"reg.html",locals())
    else:
        form=UserForm()
        return render(request,"reg.html",locals())