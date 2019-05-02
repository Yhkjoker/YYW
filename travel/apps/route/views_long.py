# _*_ encoding:utf-8 _*_
import ast


from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


from .models import TravelTheme, City,Utils
from apps.utils.constant_service import CONSTANT

# Create your views here.

class GetList(View):
    """
    筛选基类
    """
    def get(self,request,big_type):
        context = {}
        big_type = big_type
        month = request.GET.get('month', '0')
        area = int(request.GET.get('area', 1)) #int是为了方便在模版中与city.vo.id 作比较，为了actice效果
        days = request.GET.get('days', '0')
        price = request.GET.get('price', '0')

        theme_list = TravelTheme.objects.filter(big_type=big_type)
        if month != '0':
            theme_list = theme_list.filter(fit_month=int(month))

        if area != 1:
            theme_list = theme_list.filter(area_id=int(area))

        if days != '0':
            theme_list = theme_list.filter(days=int(days))

        if price != '0':
            theme_list = theme_list.filter(price=int(price))


        # 筛选当前类型的城市
        city = City.objects.filter(type__contains=big_type)
        # 获取当前旅游类型的月份
        context['all_month'] = CONSTANT.month
        # 获取当前旅游类型的所有城市或区域
        context['all_area'] = city
        # 获取当前旅游类型的所有天数
        context['all_days'] = CONSTANT.days
        # 获取当前旅游类型所有价格
        context['all_price'] = CONSTANT.price

        location = ''
        for i in city:
            if area == i.id:
                location = i.area
        print(CONSTANT.target_url[big_type])
        context['target_url'] = CONSTANT.target_url[big_type]
        context['location'] = location
        context['type'] = big_type
        context['month'] = month
        context['area'] = area
        context['days'] = days
        context['price'] = price

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(theme_list, 1, request=request)
        theme_list = p.page(page)

        context['theme_list'] = theme_list

        return render(request, 'Long_list.html', context)


class LongListView(GetList):
    """
    长途旅行
    """
    def get(self,request):
        return super(LongListView,self).get(request,'ct')


class ShortListView(GetList):
    """
    短途旅行
    """
    def get(self,request):
        return super(ShortListView,self).get(request,'dt')


class IdenticalListView(GetList):
    """
    同城旅行
    """
    def get(self,request):
        return super(IdenticalListView,self).get(request,'tc')


