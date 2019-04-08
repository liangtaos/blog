#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :  17:48
# @Author : cold
# @File : adminforms.py


from django import forms

class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)

