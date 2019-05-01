# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-01 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0010_auto_20190501_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utils',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(default='', max_length=1000, verbose_name='时间月份')),
                ('area', models.CharField(default='', max_length=1000, verbose_name='区域')),
                ('days', models.CharField(default='', max_length=1000, verbose_name='天数')),
                ('price', models.CharField(default='', max_length=1000, verbose_name='价格')),
                ('type', models.CharField(choices=[('0', '同城'), ('1', '短途'), ('2', '长途')], default='', max_length=1000, verbose_name='路线类型')),
            ],
            options={
                'verbose_name': '筛选',
                'verbose_name_plural': '筛选',
            },
        ),
        migrations.RemoveField(
            model_name='traveltheme',
            name='max_price',
        ),
        migrations.RemoveField(
            model_name='traveltheme',
            name='min_price',
        ),
        migrations.AddField(
            model_name='traveltheme',
            name='price',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, help_text='每个数字代表一个价格', verbose_name='价格'),
        ),
    ]