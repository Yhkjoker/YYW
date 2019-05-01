# _*_ encoding:utf-8 _*_

from django.db import models
from datetime import datetime

from route.models import *
from users.models import *
# Create your models here.


class OrderDetail(models.Model):
    """
    订单
    """
    order_user = models.ForeignKey(UserProfile,on_delete=models.CASCADE, null=True, blank=True, verbose_name=u'订单所属人')
    order_tours = models.IntegerField(verbose_name='订单所属主题',help_text='关联旅行队伍',null=True)
    contact = models.CharField(max_length=8, verbose_name=u'紧急联系人')
    contact_way = models.CharField(max_length=11, verbose_name=u'联系方式')
    s_friend = models.CharField(max_length=2, choices=(('0', '有'), ('1', '无')), default='0', verbose_name=u'是否有睡友')
    remark = models.CharField(max_length=100, verbose_name=u'备注')
    number = models.IntegerField(verbose_name=u'出行人数')
    total = models.IntegerField(verbose_name=u'总额')
    add_date = models.DateField(auto_now_add=True, verbose_name=u'下单时间')
    status = models.IntegerField(verbose_name='订单状态',help_text='0:已提交，1：已付款，2：已退款',null=True)
    travel_buddy = models.CharField(verbose_name='出行人',max_length=50,help_text='列表形式[id1,id2.....],关联Userman',null=True)

    class Meta:
        verbose_name = u'订单详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


class TeamOrder(models.Model):
    """
    团队定制
    """
    order_user = models.ForeignKey(UserProfile,on_delete=models.CASCADE, null=True, blank=True, verbose_name=u'订单所属人')
    start_place = models.CharField(max_length=50,verbose_name='出发地')
    end_place = models.CharField(max_length=50,verbose_name='目的地')
    days = models.IntegerField(verbose_name='出发天数')
    nature = models.CharField(verbose_name='出游性质',max_length=20)
    start_time = models.DateTimeField(verbose_name='开始时间')
    end_time = models.DateTimeField(verbose_name='结束时间')
    budget = models.IntegerField(verbose_name='出游预算')
    people_num = models.IntegerField(verbose_name='出游人数')
    remarks = models.CharField(verbose_name='备注',max_length=50, help_text=u'最长字段为50')
    name = models.CharField(verbose_name='姓名',max_length=10)
    phone = models.CharField(verbose_name='手机', max_length=11)
    add_time = models.DateField(verbose_name=u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = '团队定制'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
