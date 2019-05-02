# _*_ encoding:utf-8 _*_
"""travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve
from .settings import MEDIA_ROOT

from users.views import *
from route.views import *
from route.views_long import *
from orders import views as orderview


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^yyw/$', IndexView.as_view(), name="index"),
    # 账号登录与注册
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    # 加载验证码
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="useractive"),
    url(r'^forget$', ForgetView.as_view(), name="forget"),
    url(r'^retrievepwd/(?P<active_code>.*)/$', RetrievePwdView.as_view(), name="retrievepwd"),
    url(r'^reset_pwd/$', ResetpwdView.as_view(), name="resetpwd"),
    # 列表展示
    url(r'^identical_list/$', IdenticalListView.as_view(), name="identical_list"),
    url(r'^long_list/$', LongListView.as_view(), name="long_list"),
    url(r'^short_list/$', ShortListView.as_view(), name="short_list"),
    url(r'^list_details/$', ListDetailsView.as_view(), name="list_details"),
    # 处理静态文件的函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # 订单提交
    url(r'^order/', include('orders.urls', namespace='order')),

    url(r'^order_signup/$', OrderSignUpView.as_view(), name="order_signup"),
    # 底部
    url(r'^common_problem/$', CommonProblemView.as_view(), name="common_problem"),
    url(r'^contact_us/$', ContactUsView.as_view(), name="contact_us"),
    url(r'^join_us/$', JoinUs.as_view(), name="join_us"),
    url(r'^disclaimer/$', DisclaimerView.as_view(), name="disclaimer"),
    url(r'^base/$', BaseView.as_view(), name='base'),

    url(r'^celery/',orderview.celery,name='celery'),
    url(r'^log/',orderview.log_test,name='log'),
]
