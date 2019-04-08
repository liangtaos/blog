#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :  15:19
# @Author : cold
# @File : test.py

from django.contrib.auth.models import User
from django.test.utils import override_settings
from .models import  Category

from django.test import TestCase
from pprint import pprint as pp
from django.db import connection
import time
class TestCategory(TestCase):
    def setUp(self):
        user = User.objects.create_user('liangtao','codl@163.com','passwd')
        # for i in range(10):
        #     category_name = 'cate_name_{0}'.format(i)
        #     Category.objects.create(name=category_name,owner=user)
        Category.objects.bulk_create([
            Category(name='cate_bulk_%s'%i,owner=user)
            for i in range(10,20)
        ])
    @override_settings(DEBUG=True)
    def test_filter(self):
        # print(time.ctime())
        category = Category.objects.all()
        cate = category.exclude(status=0).filter(owner=1).order_by('-id')
        # for i in cate:
        #     print(i.name)
        # print(category)
        # cate = category.filter(status=1)
        # for i in cate:
        #     print(i.created_time)
        # print(cate)
        # print('*'*50)
        # pp(connection.queries)
        # print('*'*50)
        # print(len(cate))

<<<<<<< HEAD
    # def test_value(self):
    #     print('3333333333333333333333333333333333333333'*3)
    #     category = Category.objects.values('name')
    #     print(category)
    #     print('4'*45)
    #     category = Category.objects.values_list('name')
    #     print(category)
    #     print('5'*55)
    #     category = Category.objects.values_list('name',flat=True)
    #     print(category)
    #     for cate in category:
    #         print(cate)

    @override_settings(DEBUG=True)
    def test(self):
        # user = User.objects.create_user('liangtao2', 'codl@163.com', 'passwd')
        # Category.objects.create()
        # cat = Category.objects.create(name='cate_bulk_12',owner=user)
        # cate = Category.objects.get_or_create(name='cate_bulk_34')
        # print(cate.name)
        # for i in cate:
        #     print(i.name)
        # print('-'*200)
        # # cate = cate.filter(name='cate_bulk_19')
        # # cate = cate.order_by('name').reverse()
        # cate = cate.values('owner__username').distinct()
        # print(cate)
        # for i in cate:
        #     print(i['owner__username'])
        # cat = Category.objects.update()
        # print(cat)
        # cat = Category.objects.filter(name__contains='cate')
        # cates = Category.objects.filter(name__in=cat)
        # Category.objects()
        # print(cates)
        # for i in cates:
        #     print(i.name)
        # print('-'*100)
        # pp(connection.queries)
=======

    def test_value(self):
        print('3333333333333333333333333333333333333333'*3)
        category = Category.objects.values('name')
        print(category)
        print('4'*45)
        category = Category.objects.values_list('name')
        print(category)
        print('5'*55)
        category = Category.objects.values_list('name',flat=True)
        print(category)
        for cate in category:
            print(cate)
>>>>>>> 0c1c352a993a535c090b89d51c0eb98d0fa2fbf4
