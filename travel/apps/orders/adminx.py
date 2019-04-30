# _*_ encoding:utf-8 _*_

import xadmin

from .models import *


class OrderDetailAdmin(object):
    list_display = ['order_user', 'order_tours', 'contact', 'contact_way', 's_friend', 'remark', 'number', 'total','add_date','status','travel_buddy']


class TeamOrderAdmin(object):
    list_display = ['order_user', 'start_place', 'end_place', 'days', 'nature', 'start_time', 'end_time', 'budget', 'people_num', 'remarks', 'name', 'phone']


xadmin.site.register(OrderDetail, OrderDetailAdmin)
xadmin.site.register(TeamOrder, TeamOrderAdmin)

