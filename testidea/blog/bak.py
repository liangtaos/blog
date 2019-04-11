#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :  16:13
# @Author : cold
# @File : bak.py


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Post,Tag, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from config.models import Link, SideBar
from comment.models import Comment


def getBaseData():
    cates = Category.objects.all()
    showCate = []
    hiddenCate = []
    for cate in cates:
        if cate.is_nav:
            showCate.append(cate)
        else:
            hiddenCate.append(cate)

    hotPosts = Post.objects.all()[:10]
    sidebar = SideBar.objects.all().order_by('display_type')
    comment = Comment.objects.all().order_by('created_time')[:5]
    return {
        'showCate': showCate,
        'hiddenCate': hiddenCate,
        'hotPosts': hotPosts,
        'sidebar': sidebar,
        'comment': comment,
    }



def index(request, category_id=None, tag_id=None):
    queryset = Post.objects.all()
    page_size = 3
    if category_id:
        queryset = queryset.filter(category_id=category_id)
    elif tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Exception as e:
            return HttpResponse(404)
        queryset = tag.tags.all()
    if not queryset:
        return HttpResponse(404)

    paginator = Paginator(queryset, page_size)   # 获取分页对象
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        queryset = paginator.page(currentPage)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)



    context = {
        'posts': queryset,
        'page': currentPage,
        'paginator': paginator,
        'category_id': category_id,
        'tag_id': tag_id,
    }
    context.update(getBaseData())
    return render(request, 'list.html', context=context,)



def detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Exception as DoesNotExist:
        return HttpResponse(404)
    context = {
        'post': post
    }
    context.update(getBaseData())
    return render(request, 'detail.html', context=context)