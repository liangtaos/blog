# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20190417_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.CharField(max_length=2000, verbose_name='评论目标'),
        ),
    ]