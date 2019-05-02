# _*_ encoding:utf-8 _*_
import ast


from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


from .models import TravelTheme, City,Utils
from apps.utils.constant_service import CONSTANT

# Create your views here.

class LongListView(View):
    def get(self, request):
        context = {}
        month = request.GET.get('month','0')
        area = request.GET.get('area','1')
        days = request.GET.get('days','0')
        price = request.GET.get('price','6')
        theme_list = TravelTheme.objects.filter(fit_month=month,area=area,days=days,price=price)

        screen = CONSTANT
        # 获取当前旅游类型的月份
        context['all_month'] = CONSTANT.month
        # 获取当前旅游类型的所有城市或区域
        context['all_area'] = CONSTANT.area_long
        # 获取当前旅游类型的所有天数
        context['all_days'] = CONSTANT.days
        # 获取当前旅游类型所有价格
        context['all_price'] = CONSTANT.price


        for i in CONSTANT.area_long:
            if i['key'] == str(area):
                location = i['value']

        context['location'] = location
        context['theme_list'] = theme_list
        context['month'] = month
        context['area'] = area
        context['days'] = days
        context['price'] = price

        return render(request, 'Long_list.html', context)

