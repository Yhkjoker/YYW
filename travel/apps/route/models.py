# _*_ encoding:utf-8 _*_

from django.db import models
from datetime import datetime

# Create your models here.


class City(models.Model):
    """
    城市
    """
    area = models.CharField(verbose_name=u'区域', max_length=10)

    class Meta:
        verbose_name = '所属区域'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.area


class TravelTheme(models.Model):
    """
    旅游主题
    """
    month = (('0', '全部'), ('1', '一月'), ('2', '二月'), ('3', '三月'), ('4', '四月'), ('5', '五月'), ('6', '六月'), ('7', '七月'), ('8', '八月'), ('9', '九月'), ('10', '十月'), ('11', '十一月'), ('12', '十二月'))
    big_type = models.CharField(verbose_name='旅行分类',choices=(('tc','同城旅行'),('dt','短途旅行'),('ct','长途旅行'),('zt','主题旅行')),max_length=4)
    area = models.ForeignKey(City, verbose_name=u'所在区域')
    fit_month = models.CharField(max_length=4, verbose_name=u'适宜月份', default='0', choices=month)
    price = models.IntegerField(verbose_name='价格',default=1,choices=((1,1),(2,2),(3,3),(4,4),(5,5)),help_text='每个数字代表一个价格')
    days = models.IntegerField(verbose_name='旅游天数')
    title = models.CharField(verbose_name='主题名称', max_length=50)
    route = models.CharField(verbose_name='路线',help_text='字段之间请以逗号相隔',max_length=255)
    power = models.IntegerField(verbose_name='体力', default=2, choices=((1, 1), (2,2), (3, 3), (4, 4), (5, 5)))
    describe = models.CharField(verbose_name='主题描述',max_length=255,help_text='此字段用于主页,最大长度为255')
    theme_intro = models.CharField(max_length=100, verbose_name=u'主题简介', help_text=u'最大长度为100', default='')
    theme_type = models.CharField(max_length=20, verbose_name=u'主题类别', default='')
    img = models.ImageField(upload_to="imgae/%Y/%m", verbose_name='图片')
    click_num = models.IntegerField(verbose_name='点击数量',default=0)
    add_time = models.DateField(verbose_name=u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = '旅行主题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ThemeInfo(models.Model):
    """
    主题详情
    """
    theme = models.ForeignKey(TravelTheme,on_delete=models.CASCADE,verbose_name='所属的主题')
    img = models.ImageField(upload_to="details_img/%Y/%m", verbose_name='图片')
    baidu_baike = models.CharField(verbose_name='百科介绍',max_length=255)
    attraction_port = models.CharField(verbose_name='景点',max_length=255)
    schedule = models.CharField(verbose_name='行程安排',max_length=2000,help_text='此字段为列表结构[[day1,[一点干啥，两点干啥,.....]],[day2,[]]]')
    attraction = models.CharField(verbose_name='注意事项', max_length=1000, help_text='此字段为列表')
    cost_state = models.CharField(verbose_name='费用说明', max_length=1000, help_text='此字段为列表', default='')

    class Meta:
        verbose_name = '主题详细'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.theme.title


class Tours(models.Model):
    """
    旅行队伍
    """
    theme = models.ForeignKey(TravelTheme,on_delete=models.CASCADE,verbose_name='所属的主题')
    go_off = models.CharField(verbose_name='出发时间',max_length=10, help_text=u'格式:月-日', default='')
    end_time = models.CharField(verbose_name='结束时间',max_length=10, help_text=u'格式:月-日', default='')
    team_num = models.IntegerField(verbose_name='队伍编号')
    status = models.IntegerField(verbose_name='报名状态',choices=(('1','报名'),('0','已满')))
    price = models.IntegerField(verbose_name='价格')
    max_num = models.IntegerField(verbose_name='最大人数')
    now_num = models.IntegerField(verbose_name='当前人数', default=0)

    class Meta:
        verbose_name = '报名队伍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.theme.title
