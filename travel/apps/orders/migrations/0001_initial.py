# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-21 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('route', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('0', '待付款'), ('1', '已完成'), ('2', '已取消')], default='0', max_length=5, verbose_name='订单状态')),
            ],
            options={
                'verbose_name': '我的订单',
                'verbose_name_plural': '我的订单',
            },
        ),
        migrations.CreateModel(
            name='OrderBuddy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=7, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('0', '男'), ('1', '女')], max_length=2, verbose_name='性别')),
                ('card_type', models.CharField(choices=[('0', '身份证'), ('1', '护照')], max_length=5, verbose_name='证件类型')),
                ('card', models.CharField(max_length=18, verbose_name='证件号')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('email', models.EmailField(max_length=20, verbose_name='邮箱')),
                ('price', models.IntegerField(verbose_name='价格')),
            ],
            options={
                'verbose_name': '同行人',
                'verbose_name_plural': '同行人',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=8, verbose_name='紧急联系人')),
                ('contact_way', models.CharField(max_length=11, verbose_name='联系方式')),
                ('s_friend', models.CharField(choices=[('0', '有'), ('1', '无')], default='0', max_length=2, verbose_name='是否有睡友')),
                ('remark', models.CharField(max_length=100, verbose_name='备注')),
                ('number', models.IntegerField(verbose_name='出行人数')),
                ('total', models.IntegerField(verbose_name='总额')),
                ('add_date', models.DateField(auto_now_add=True, verbose_name='下单时间')),
                ('route', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='route.Route', verbose_name='线路')),
            ],
            options={
                'verbose_name': '订单详情',
                'verbose_name_plural': '订单详情',
            },
        ),
        migrations.AddField(
            model_name='orderbuddy',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.OrderDetail', verbose_name='订单'),
        ),
        migrations.AddField(
            model_name='myorder',
            name='order_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.OrderDetail', verbose_name='订单详情'),
        ),
    ]
