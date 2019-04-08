#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :  17:48
# @Author : cold
# @File : adminforms.py

from django import forms


class PostAdminForm(forms.ModelForm):
    status = forms.BooleanField(label='是否删除', required=True)
    desc = forms.CharField(widget=forms.Textarea, label='炒药', required=False)
