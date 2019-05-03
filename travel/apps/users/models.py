# _*_ encoding:utf-8 _*_

from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.


class UserProfile(AbstractUser):
    mobile = models.CharField(max_length=11, verbose_name=u'手机号')
    card = models.CharField(max_length=18,verbose_name=u'证件号')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(verbose_name=u"验证码类型", choices=(("register",u"注册"),("forget",u"找回密码"), ("update_email",u"修改邮箱")), max_length=30)
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name


class UserMan(models.Model):
    name = models.CharField(max_length=7, verbose_name=u'姓名')
    gender = models.CharField(max_length=2, choices=(('0', '男'), ('1', '女')), verbose_name=u'性别')
    card_type = models.CharField(max_length=5, choices=(('0', '身份证'), ('1', '护照')), verbose_name=u'证件类型')
    card = models.CharField(max_length=18, verbose_name=u'证件号')
    mobile = models.CharField(max_length=11, verbose_name=u'手机号')
    email = models.EmailField(max_length=20, verbose_name=u'邮箱')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, verbose_name=u'用户')
    status = models.CharField(max_length=2, choices=(('0', '否'), ('1', '是')), default=1, verbose_name=u'添加为常用联系人')

    class Meta:
        verbose_name = u'常用出行人'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
