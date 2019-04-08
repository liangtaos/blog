#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :  15:50
# @Author : cold
# @File : custom_site.py


from django.contrib.admin import AdminSite



class CustomSite(AdminSite):
    site_header = '后台管理'
    site_title = '后台'
    index_title = '首页'



custom_site = CustomSite(name='cus_admin')