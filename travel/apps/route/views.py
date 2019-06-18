# _*_ encoding:utf-8 _*_
import ast
import json


from django.shortcuts import render
from django.shortcuts import redirect,reverse
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


class IndexView_Redict(View):
    def get(selfself,request):
        return redirect(reverse('index'))


# 主页
class IndexView(View):
    """
    主页显示
    """
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
    """
    主题详情显示
    """
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
        context['attraction_port'] = json.loads(details.attraction_port)
        context['schedule'] = json.loads(details.schedule)
        print('schedule',json.loads(details.schedule))
        context['attraction'] = json.loads(details.attraction)
        context['cost_state'] = json.loads(details.cost_state)
        theme.save()
        return render(request, 'List_details.html', context)


# 常见问题
class CommonProblemView(View):
    """
    常见问题显示
    """
    def get(self, request):
        return render(request, 'Common_Problem.html', {})


# 联系我们
class ContactUsView(View):
    """
    联系我们显示
    """
    def get(self, request):
        return render(request, 'Contact_Us.html', {})


# 免责说明
class DisclaimerView(View):
    """
    免责说明显示
    """
    def get(self, request):
        return render(request, 'Disclaimer.html', {})


# 加入我们
class JoinUs(View):
    """
    加入我们显示
    """
    def get(self, request):
        return render(request, 'Join_Us.html', {})

