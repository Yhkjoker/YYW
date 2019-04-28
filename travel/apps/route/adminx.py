# _*_ encoding:utf-8 _*_

import xadmin
from .models import *


class TravelThemeAdmin(object):
    list_display = ['big_type','title','days','route','power','price','describe','introduce','mouth','img','station','click_num']


class ThemeInfoAdmin(object):
    list_display = ['theme','baidu_baike','attraction_port','img','schedule','attraction']


class ToursAdmin(object):
    list_display = ['theme','date','team_num','status','price','max_num','now_num']


xadmin.site.register(TravelTheme, TravelThemeAdmin)
xadmin.site.register(ThemeInfo, ThemeInfoAdmin)
xadmin.site.register(Tours, ToursAdmin)