# _*_ encoding:utf-8 _*_

from django.db import models

# Create your models here.


class RouteType(models.Model):
    route_type = models.CharField(max_length=20, verbose_name=u'线路类型')

    class Meta:
        verbose_name = u'线路分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.route_type


class Route(models.Model):
    type = models.ForeignKey(RouteType, on_delete=models.CASCADE, null=True, blank=True, verbose_name=u'线路类型')
    des = models.CharField(max_length=100, verbose_name=u'简要说明')
    start_date = models.DateField(verbose_name=u'开始日期')
    end_date = models.DateField(verbose_name=u'结束日期')
    time = models.IntegerField(verbose_name=u'花费天数')
    min_price = models.IntegerField(verbose_name=u'最低价格')
    max_price = models.IntegerField(verbose_name=u'最高价格')
    title = models.CharField(max_length=50, verbose_name=u'标题')
    route = models.CharField(max_length=50,verbose_name=u'行程')
    power = models.IntegerField(verbose_name=u'所需体力')
    click = models.IntegerField(verbose_name=u'点击数')
    date = models.DateField(auto_now_add=True, verbose_name=u'添加时间')
    image = models.ImageField(upload_to="imgae/%Y/%m", verbose_name=u'图片')

    class Meta:
        verbose_name = u'线路'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class TravelTeam(models.Model):
    start_date = models.DateField(verbose_name=u'开始日期')
    end_date = models.DateField(verbose_name=u'结束日期')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, null=True, blank=True, verbose_name=u'路线')
    team = models.IntegerField(verbose_name=u'队伍编号')
    status = models.CharField(max_length=2, choices=(('0', '报名'), ('1', '已满')), default=u'0', verbose_name=u'队伍状态')

    class Meta:
        verbose_name = u'队伍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.team


class RouteDetails(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name=u'线路')
    image = models.ImageField(upload_to="image/%Y/%m")

    class Meta:
        verbose_name = u'线路详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class RouteIntro(models.Model):
    details = models.ForeignKey(RouteDetails, on_delete=models.CASCADE, null=True, blank=True, verbose_name=u'详情')
    text = models.TextField(verbose_name=u'简介')

    class Meta:
        verbose_name = u'线路简介'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class RoutePlan(models.Model):
    details = models.ForeignKey(RouteDetails, on_delete=models.CASCADE, null=True, blank=True, verbose_name=u'详情')
    text = models.TextField(verbose_name=u'安排')

    class Meta:
        verbose_name = u'行程安排'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class Announcement(models.Model):
    details = models.ForeignKey(RouteDetails, on_delete=models.CASCADE, null=True, blank=True, verbose_name=u'详情')
    text = models.TextField(verbose_name=u'注意事项')

    class Meta:
        verbose_name = u'注意事项'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class FeeDescription(models.Model):
    details = models.ForeignKey(RouteDetails, on_delete=models.CASCADE, null=True, blank=True, verbose_name=u'详情')
    text = models.TextField(verbose_name=u'费用说明')

    class Meta:
        verbose_name = u'费用说明'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id

