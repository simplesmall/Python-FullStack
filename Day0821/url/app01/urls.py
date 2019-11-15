
from django.conf.urls import url,include

from app01 import views

urlpatterns = [
    # 正则匹配且分组
    url(r'^article/2003/',views.year_article),
    url(r'^article/(\d{4})/$',views.year_article),
    # 有名分组
    url(r'^article/(?p<year>\d{4})/(?p<month>\d{2})/',views.year_article_two)
]
