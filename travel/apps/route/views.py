# _*_ encoding:utf-8 _*_
import ast


from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


from .models import *
from utils.constant_service import CONSTANT

from .models import TravelTheme, City
from apps.utils.redis_connect import REDIS
# Create your views here.


class BaseView(View):
    def get(self, request):
        return render(request, "details.html")


# 主页
class IndexView(View):
    def get(self, request):
        context = {}
        all_theme = TravelTheme.objects.all()
        hot_route = all_theme.order_by('-click_num')[:2]
        hot_tc = all_theme.filter(big_type='tc').order_by('-click_num')[0]
        hot_dt = all_theme.filter(big_type='dt').order_by('-click_num')[0]
        hot_ct = all_theme.filter(big_type='ct').order_by('-click_num')[0]
        try:
            hot_routes = ast.literal_eval(REDIS.get('hot_route'))
        except:
            hot_routes = []
        context['lunbotu'] = hot_route
        context['hot_route'] = hot_routes
        return render(request, 'index.html', context)


# 主题详情
class ListDetailsView(View):
    def get(self, request, id):
        context={}
        theme = TravelTheme.objects.get(id=id)
        theme.click_num += 1
        context['theme_id'] = id
        context['title'] = theme.title
        type= theme.big_type
        context['days'] = theme.days
        context['type'] = CONSTANT.type(type)
        tours = Tours.objects.filter(theme_id=int(id))
        details = ThemeInfo.objects.get(theme_id=int(id))
        context['tours'] = tours
        context['details'] = details
        context['baike'] = details.baidu_baike
        theme.save()
        return render(request, 'List_details.html', context)


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

