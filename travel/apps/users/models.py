# _*_ encoding:utf-8 _*_

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    mobile = models.CharField(max_length=11, verbose_name=u'手机号')
    card = models.CharField(max_length=18,verbose_name=u'证件号')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class UserMan(models.Model):
    name = models.CharField(max_length=7, verbose_name=u'姓名')
    gender = models.CharField(max_length=2, choices=(('0', '男'), ('1', '女')), verbose_name=u'性别')
    card_type = models.CharField(max_length=5, choices=(('0', '身份证'), ('1', '护照')), verbose_name=u'证件类型')
    card = models.CharField(max_length=18, verbose_name=u'证件号')
    mobile = models.CharField(max_length=11, verbose_name=u'手机号')
    email = models.EmailField(max_length=20, verbose_name=u'邮箱')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, verbose_name=u'用户')
    status = models.CharField(max_length=2, choices=(('0', '公开'), ('1', '默认')), default=0, verbose_name=u'设为默认联系人')

    class Meta:
        verbose_name = u'常用出行人'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
