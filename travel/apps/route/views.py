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


# 同城
class IdenticalListView(View):
    def get(self, request):
        # 获取所有旅游的主题
        all_theme = TravelTheme.objects.all()
        # 获取所有的城市
        all_area = City.objects.all()

        area = request.GET.get('area', '')
        month = request.GET.get('month', '')
        days = request.GET.get('days', '')
        price = request.GET.get('price', '')

        # 区域筛选
        if area:
            all_theme = all_theme.filter(area_id=int(area))
        # 月份筛选
        if month:
            all_theme = all_theme.filter(Q(fit_month=month)|Q(fit_month='0'))
        # 天数筛选
        if days:
            if int(days) < 4:
                all_theme = all_theme.filter(days=int(days))
            else:
                days = '4'
                all_theme = all_theme.filter(days__gte=int(days))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_theme, 5, request=request)

        theme = p.page(page)
        return render(request, 'Identical_list.html', {
            'all_theme': theme,
            'all_area': all_area,
            'area':area,
            'month':month,
            'days':days,
        })


# 短途
class ShortListView(View):
    def get(self, request):
        return render(request, 'Short_list.html', {})


# 长途
class LongListView(View):
    def get(self, request):
        return render(request, 'Long_list.html', {})


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

