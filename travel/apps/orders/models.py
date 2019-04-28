# _*_ encoding:utf-8 _*_

from django.db import models
from route.models import *
from users.models import *
# Create your models here.


class OrderDetail(models.Model):
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
        return self.id
