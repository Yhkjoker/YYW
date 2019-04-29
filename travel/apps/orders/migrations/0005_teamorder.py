# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-29 19:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0004_auto_20190428_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_place', models.CharField(max_length=50, verbose_name='出发地')),
                ('end_place', models.CharField(max_length=50, verbose_name='目的地')),
                ('days', models.IntegerField(verbose_name='出发天数')),
                ('nature', models.CharField(max_length=20, verbose_name='出游性质')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('budget', models.IntegerField(verbose_name='出游预算')),
                ('people_num', models.IntegerField(verbose_name='出游人数')),
                ('remarks', models.IntegerField(verbose_name='备注')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('phone', models.IntegerField(verbose_name='手机')),
                ('order_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='订单所属人')),
            ],
        ),
    ]
