from django.contrib import admin

# Register your models here.
import xadmin
from .models import Post,Category,Tag, TopNav
from django.utils.html import format_html
from testidea.adminx import BaseOwnerAdmin
from django.urls import reverse

from .adminforms import PostAdminForm


class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm    # 通过adminform处理
    list_display = ['preview','title', 'category', 'owner','status_show', 'created_time', 'operator', 'de', 'status']   # 展示
    search_fields = ['title', 'category__name', 'owner__username']   # 搜索
    exclude = ['owner', 'html', 'pv', 'uv']
    list_filter = ['status']

    def preview(self, obj):
        return format_html(
            '<a href="/post/%s.html">预览</a>'%(obj.id),
        )

    preview.short_description = '查看'
    def operator(self,obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('xadmin:blog_post_change',args=(obj.id,))
        )
    operator.short_description = '操作'
    # 删除
    def de(self, obj):
        return format_html(
            '<a href="{}">删除 </a>',
            reverse('xadmin:blog_post_delete',args=(obj.id,))
        )
    de.short_description = '删除'

    def save_model(self, request, obj, form, change):
        # print(self,request,obj,form, change)
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request,obj,form, change)

# @admin.register(Category,site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'owner', 'created_time']

# @admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'owner', 'created_time']


# @admin.register(TopNav, site=custom_site)
class TopNavAdmin(BaseOwnerAdmin):
    list_display = ['name', 'url', 'owner', 'status', 'created_time']

xadmin.site.register(Post,PostAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Tag,TagAdmin)

