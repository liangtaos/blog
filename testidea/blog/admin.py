from django.contrib import admin

# Register your models here.

from .models import Post,Category,Tag
from django.utils.html import format_html
from testidea.custom_site import custom_site
from testidea.BaseAdmin import BaseOwnerAdmin
from django.urls import reverse

from .adminforms import PostAdminForm

@admin.register(Post,site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    # form = PostAdminForm    # 通过adminform处理
    list_display = ['title', 'category', 'owner','status_show', 'created_time', 'operator', 'de', 'status']   # 展示
    search_fields = ['title', 'category__name', 'owner__username']   # 搜索
    exclude = ['owner']
    list_filter = ['status']

    def operator(self,obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change',args=(obj.id,))
        )
    operator.short_description = '操作'
    # 删除
    def de(self, obj):
        return format_html(
            '<a href="{}">删除 </a>',
            reverse('cus_admin:blog_post_delete',args=(obj.id,))
        )
    de.short_description = '删除'

    def save_model(self, request, obj, form, change):
        print(self,request,obj,form, change)
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request,obj,form, change)

@admin.register(Category,site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'owner', 'created_time']

@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'owner', 'created_time']

# admin.site.register(Post,PostAdmin,site=custom_site)
# admin.site.register(Category,CategoryAdmin)
# admin.site.register(Tag,TagAdmin)

