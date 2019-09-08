from django.conf.urls import url
from login.views import index, center, edit, form1

urlpatterns = [
    # index/
    # url的第一参数是:正则
    # url的第二参数是:视图函数名
    # pay/order/
    url(r'^index\.html/$', index),
    url(r'^center\.html/$', center),
    url(r'^edit\.html/$', edit),
    url(r'^edit\.html/update', form1),

]
