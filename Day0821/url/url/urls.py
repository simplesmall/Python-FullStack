"""url URL Configuration

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
from django.conf.urls import url,include

from app01 import views

urlpatterns = [
    url(r'^$',views.index),
    # path('admin/', admin.site.urls),
    # # 正则匹配且分组
    # path(r'^article/(\d{4})/$',views.year_article),
    # # 有名分组
    # path(r'^article/(?p<year>\d{4})/(?p<month>\d{2})/',views.year_article_two)
    url(r'^app01/',include('app01.urls'))
]
