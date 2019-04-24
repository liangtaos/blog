#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :  15:26
# @Author : cold
# @File : api.py


from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Post, Category, Tag
from django.contrib.auth.models import User

# User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username',
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer








# Category
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'url', 'name', 'created_time',
        )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Post
class PostSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        read_only= True,
        slug_field='name'
    )
    tag = serializers.SlugRelatedField(
        many=True,
        read_only= True,
        slug_field='name'
    )
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Post
        fields = (
            'id',
            'title',  'desc', 'tag',
            'category',  'created_time', 'pv', 'uv',
            'owner',
                  )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Tag
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id', 'name', 'created_time',
        )

class TagDetailSerializer(serializers.ModelSerializer):
    posts = PostSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = Tag
        fields = (
            'url',
            'id', 'name', 'created_time','posts'
        )


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = TagDetailSerializer
        return super(TagViewSet, self).retrieve(request, *args, **kwargs)
