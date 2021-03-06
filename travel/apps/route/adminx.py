# _*_ encoding:utf-8 _*_

import xadmin
from .models import *


class ThemeInfoInline(object):
    model = ThemeInfo
    extra = 0


class ToursInline(object):
    model = Tours
    extra = 0


class TravelThemeAdmin(object):
    list_display = ['big_type', 'area', 'fit_month', 'days', 'title', 'price', 'img', 'click_num']
    readonly_fields = ['click_num']
    ordering = ['-click_num']
    inlines = [ThemeInfoInline, ToursInline]


class ThemeInfoAdmin(object):
    list_display = ['theme', 'baidu_baike', 'attraction_port', 'img', 'schedule', 'attraction', 'cost_state']


class ToursAdmin(object):
    list_display = ['theme', 'go_off', 'end_time', 'team_num', 'status', 'price', 'max_num', 'now_num']


class CityAdmin(object):
    list_display = ['area']


xadmin.site.register(City, CityAdmin)
xadmin.site.register(TravelTheme, TravelThemeAdmin)
xadmin.site.register(ThemeInfo, ThemeInfoAdmin)
xadmin.site.register(Tours, ToursAdmin)
