# _*_ encoding:utf-8 _*_

import xadmin

from .models import MyOrder,OrderDetail,OrderBuddy


class OrderDetailAdmin(object):
    list_display = ['route', 'contact', 'contact_way', 's_friend', 'remark', 'number', 'total', 'add_date']
    search_fields = ['route', 'number', 'total']
    list_filter = ['route', 'number', 'total']


class MyOrderAdmin(object):
    list_display = ['status']
    search_fields = ['status']
    list_filter = ['status']


class OrderBuddyAdmin(object):
    list_display = ['name', 'gender', 'card_type', 'card', 'mobile', 'email', 'price']
    search_fields = ['name', 'gender', 'card_type', 'card', 'mobile', 'email', 'price']
    list_filter = ['name', 'gender', 'card_type', 'price']


xadmin.site.register(OrderDetail, OrderDetailAdmin)
xadmin.site.register(OrderBuddy, OrderBuddyAdmin)
xadmin.site.register(MyOrder, MyOrderAdmin)

