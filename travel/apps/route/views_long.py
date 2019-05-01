# _*_ encoding:utf-8 _*_
import ast


from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


from .models import TravelTheme, City,Utils

# Create your views here.

class LongListView(View):
    def get(self, request):
        context = {}
        month = request.GET.get('month','0')
        area = request.GET.get('area','1')
        days = request.GET.get('days','0')
        price = request.GET.get('price','6')
        theme_list = TravelTheme.objects.filter(fit_month=month,area=area,days=days,price=price)

        screen = Utils.objects.get(type='0')
        # 获取当前旅游类型的月份
        all_month = screen.month
        context['all_month'] = ast.literal_eval(all_month)
        # 获取当前旅游类型的所有城市或区域
        all_area = screen.area
        context['all_area'] = ast.literal_eval(all_area)
        print(all_area)
        # 获取当前旅游类型的所有天数
        all_days = screen.days
        context['all_days'] = ast.literal_eval(all_days)
        # 获取当前旅游类型所有价格
        all_price = screen.price
        context['all_price'] = ast.literal_eval(all_price)

        context['theme_list'] = theme_list
        context['month'] = month
        context['area'] = area
        context['days'] = days
        context['price'] = price

        return render(request, 'Long_list.html', context)

