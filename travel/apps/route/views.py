# _*_ encoding:utf-8 _*_

from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import TravelTheme, City
# Create your views here.


class BaseView(View):
    def get(self, request):
        return render(request, "details.html")


# 主页
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})


# 团队定制
class CustomizedView(View):
    def get(self, request):
        return render(request, 'Customized.html', {})


# 主题详情
class ListDetailsView(View):
    def get(self, request):
        return render(request, 'List_details.html', {})


# 订单填写
class OrderSignUpView(View):
    def get(self, request):
        return render(request, 'Orders_signup.html', {})


# 常见问题
class CommonProblemView(View):
    def get(self, request):
        return render(request, 'Common_Problem.html', {})


# 联系我们
class ContactUsView(View):
    def get(self, request):
        return render(request, 'Contact_Us.html', {})


# 免责说明
class DisclaimerView(View):
    def get(self, request):
        return render(request, 'Disclaimer.html', {})


# 加入我们
class JoinUs(View):
    def get(self, request):
        return render(request, 'Join_Us.html', {})

