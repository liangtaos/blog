#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :  17:48
# @Author : cold
# @File : adminforms.py

from ckeditor.fields import RichTextField
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostAdminForm(forms.ModelForm):
    # desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='内容')

