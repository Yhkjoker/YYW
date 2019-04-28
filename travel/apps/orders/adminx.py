# _*_ encoding:utf-8 _*_

import xadmin

from .models import *


class OrderDetailAdmin(object):
    list_display = ['order_user', 'order_tours_id', 'contact', 'contact_way', 's_friend', 'remark', 'number', 'total','add_date','status','travel_buddy']

xadmin.site.register(OrderDetail, OrderDetailAdmin)

