# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-03-31 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=2000, verbose_name='评论')),
                ('nickname', models.CharField(max_length=20, verbose_name='昵称')),
                ('website', models.URLField(blank=True, verbose_name='网站')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='文章')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]