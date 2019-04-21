# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-21 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190417_1533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time', '-id'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AddField(
            model_name='post',
            name='is_markdown',
            field=models.BooleanField(default=True, verbose_name='支持Markdown格式'),
        ),
    ]