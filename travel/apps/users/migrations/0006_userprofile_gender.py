# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-08 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190503_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('0', '男'), ('1', '女'), ('2', '隐藏')], default='2', max_length=5, verbose_name='性别'),
        ),
    ]
