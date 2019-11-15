"""ORM2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from  django.conf.urls import url

from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addrecord/', views.addrecord),
    path('delrecord/', views.delrecord),
    path('query',views.query),
    path('query2',views.query2),
    path('books/',views.book_view),
    path('books/add/',views.book_add),
    # 设置默认打开的页面
    url(r'^$',views.book_view),
    re_path("^books/edit/(?P<edit_book_id>\d+)$",views.book_edit),
    re_path("^books/del/(?P<book_del_id>\d+)$",views.book_del),
]
