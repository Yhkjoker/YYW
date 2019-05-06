# _*_ encoding:utf-8 _*_

from django.conf.urls import url

from .views import TeamOrderView, AddOrderView, OrderPayView


urlpatterns = [
    url('^team/$', TeamOrderView.as_view(), name='team'),
    url('^add/$', AddOrderView.as_view(), name='add_order'),
    url('^order/$', AddOrderView.as_view(), name='order'),
    url('^pay/$', OrderPayView.as_view(), name='pay'),
]