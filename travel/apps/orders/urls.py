# _*_ encoding:utf-8 _*_

from django.conf.urls import url

from .views import *


urlpatterns = [
    url('^team/$', TeamOrderView.as_view(), name='team'),
    url('^add/$', AddOrderView.as_view(), name='add_order'),
    url('^order/$', AddOrderView.as_view(), name='order'),
    url('^pay/$', OrderPayView.as_view(), name='pay'),
    url('^order_new/$', OrderNewView.as_view(), name='order_new'),
    url('^order_his/$', OrderHisView.as_view(), name='order_his'),
    url('^my_info/$', MyInfoView.as_view(), name='my_info'),
    url('^update_info/$', UpdateInfoView.as_view(), name='update_info'),
    url('^update_mobile/$', UpdateMobileView.as_view(), name='update_mobile'),
    url('^update_email/$', UpdateEmailView.as_view(), name='update_email'),
    url('^update_man/$', UpdateManView.as_view(), name='update_man'),
]