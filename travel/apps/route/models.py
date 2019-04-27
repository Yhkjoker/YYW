# _*_ encoding:utf-8 _*_

from django.db import models

# Create your models here.

class TravelTheme(models.Model):
    big_type = models.CharField(verbose_name='旅行分类',choices=(('tc','同城旅行'),('dt','短途旅行'),('ct','长途旅行'),('zt','主题旅行')),max_length=4)
    title = models.CharField(verbose_name='主题名称',max_length=50)
    days = models.IntegerField(verbose_name='所需时间')
    route = models.CharField(verbose_name='路线',help_text='此字段所输入类型为列表',max_length=255)
    power = models.IntegerField(verbose_name='体力',default=3)
    price = models.CharField(verbose_name='价格',max_length=50)
    describe = models.CharField(verbose_name='主题描述',max_length=50,help_text='此字段用于主页')
    introduce = models.CharField(verbose_name='主题简介',max_length=255)
    mouth = models.IntegerField(verbose_name='出发月份')
    img = models.ImageField(upload_to="imgae/%Y/%m", verbose_name='图片')
    station = models.CharField(verbose_name='旅行地点',max_length=10,help_text='同城旅行为local，短途旅行为area，长途旅行直接输入区域')
    click_num = models.IntegerField(verbose_name='点击数量')


    class Meta:
        verbose_name = '旅行主题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ThemeInfo(models.Model):
    theme = models.ForeignKey(TravelTheme,on_delete=models.CASCADE,verbose_name='所属的主题')
    baidu_baike = models.CharField(verbose_name='百科介绍',max_length=255)
    attraction_port = models.CharField(verbose_name='景点',max_length=255)
    img = models.ImageField(upload_to="imgae/%Y/%m", verbose_name='图片')
    schedule = models.CharField(verbose_name='行程安排',max_length=2000,help_text='此字段为列表结构[[day1,[一点干啥，两点干啥,.....]],[day2,[]]]')
    attraction = models.CharField(verbose_name='注意事项',max_length=1000,help_text='此字段为列表')


    class Meta:
        verbose_name = '主题详细信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.theme.title


class Tours(models.Model):
    theme = models.ForeignKey(TravelTheme,on_delete=models.CASCADE,verbose_name='所属的主题')
    date = models.CharField(verbose_name='旅行日期',max_length=50)
    team_num = models.IntegerField(verbose_name='团队数量')
    status = models.IntegerField(verbose_name='报名状态',choices=(('bm',1),('ym',0)))
    price = models.IntegerField(verbose_name='价格')
    max_num = models.IntegerField(verbose_name='最大人数')
    now_num = models.IntegerField(verbose_name='当前人数')


    class Meta:
        verbose_name = '报名队伍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.theme.title
