# _*_ encoding:utf-8 _*_

from django.db import models
from route.models import Route

# Create your models here.


class OrderDetail(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, null=True, blank=True, verbose_name='线路')
    contact = models.CharField(max_length=8, verbose_name=u'紧急联系人')
    contact_way = models.CharField(max_length=11, verbose_name=u'联系方式')
    s_friend = models.CharField(max_length=2, choices=(('0', '有'), ('1', '无')), default='0', verbose_name=u'是否有睡友')
    remark = models.CharField(max_length=100, verbose_name=u'备注')
    number = models.IntegerField(verbose_name=u'出行人数')
    total = models.IntegerField(verbose_name=u'总额')
    add_date = models.DateField(auto_now_add=True, verbose_name=u'下单时间')

    class Meta:
        verbose_name = u'订单详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class OrderBuddy(models.Model):
    order = models.ForeignKey(OrderDetail, on_delete=models.CASCADE, null=True, blank=True, verbose_name=u'订单')
    name = models.CharField(max_length=7, verbose_name=u'姓名')
    gender = models.CharField(max_length=2, choices=(('0', '男'), ('1', '女')), verbose_name=u'性别')
    card_type = models.CharField(max_length=5, choices=(('0', '身份证'), ('1', '护照')), verbose_name=u'证件类型')
    card = models.CharField(max_length=18, verbose_name=u'证件号')
    mobile = models.CharField(max_length=11, verbose_name=u'手机号')
    email = models.EmailField(max_length=20, verbose_name=u'邮箱')
    price = models.IntegerField(verbose_name=u'价格')

    class Meta:
        verbose_name = u'同行人'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class MyOrder(models.Model):
    order_details = models.ForeignKey(OrderDetail, on_delete=models.CASCADE, null=True, blank=True, verbose_name=u'订单详情')
    status = models.CharField(max_length=5, choices=(('0', '待付款'), ('1', '已完成'), ('2', '已取消')), default='0', verbose_name='订单状态')

    class Meta:
        verbose_name = u'我的订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.status
