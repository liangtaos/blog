# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-28 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190423_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_src',
            field=models.ImageField(blank=True, upload_to='Isrc', verbose_name='图片路径'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='posts', to='blog.Tag', verbose_name='标签'),
        ),
    ]