# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-22 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190222_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='openid',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='uid',
            field=models.CharField(blank=True, help_text='微信用户绑定和CC视频统计', max_length=64, null=True, unique=True),
        ),
    ]
