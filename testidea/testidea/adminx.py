#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :  16:47
# @Author : cold
# @File : adminx.py



class BaseOwnerAdmin(object):
    # exclude = ('owner', 'html', 'pv', 'uv')

    def get_list_queryset(self):
        request = self.request
        qs = super(BaseOwnerAdmin, self).get_list_queryset()
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def save_models(self):
        if not self.org_obj:
            self.new_obj.owner = self.request.user
        return super(BaseOwnerAdmin, self).save_models()
