# _*_ encoding:utf-8 _*_

from django.conf.urls import url

from .views import TeamOrderView


urlpatterns = [
    url('^team/$', TeamOrderView.as_view(), name='team'),
]