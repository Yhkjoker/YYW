# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-03 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userman',
            name='status',
            field=models.CharField(choices=[('0', '否'), ('1', '是')], default=1, max_length=2, verbose_name='添加为常用联系人'),
        ),
    ]