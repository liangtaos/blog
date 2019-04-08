#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/4/8 21:42
# @Author: cold
# @File : BaseAdmin.py


from django.contrib import admin

class BaseOwnerAdmin(admin.ModelAdmin):
    exclude = ('owner',)

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)
