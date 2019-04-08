from django.contrib import admin

# Register your models here.

from .models import Post,Category,Tag
from django.utils.html import format_html
from testidea.custom_site import custom_site

from django.urls import reverse

from .adminforms import PostAdminForm

@admin.register(Post,site=custom_site)
class PostAdmin(admin.ModelAdmin):
    # form = PostAdminForm    # 通过adminform处理
    list_display = ['title', 'category', 'owner','status_show', 'created_time', 'operator', 'de']   # 展示
    search_fields = ['title', 'category__name', 'owner__username']   # 搜索
    # list_filter = ['category','status','tag']    #过滤器
    # save_on_top = True    # 顶部可保存
    # show_full_result_count = False   #是否显示所有的结果
    # list_display_links = ['category', 'status', 'owner']   # 可点击进入编辑页面
    # actions_on_bottom = True
    # list_editable = ('title', 'owner',)  # 可编辑
    # date_hierarchy = 'created_time'   # 时间过滤
    exclude = ['owner']
    # 编辑页面
    # fields = (
    #     ('title', 'category',),
    #     'content',
    #     'tag',
    #     # 'stat'
    #     'owner'
    # )
    # exclude = ('content',)  #不显示
    #

    list_filter = ['status']
    def operator(self,obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change',args=(obj.id,))
        )
    operator.short_description = '操作'
    # operator.allow_tags =True

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



class PostInlineAdmin(admin.StackedInline):
    fields = ['title','status','content']
    extra = 3   # 新增空的的obj的个数
    model = Post

@admin.register(Category,site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    # inlines = [PostInlineAdmin]   # 在分类界面操作Post，新增和编辑
    pass

@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    pass




# admin.site.register(Post,PostAdmin,site=custom_site)
# admin.site.register(Category,CategoryAdmin)
# admin.site.register(Tag,TagAdmin)

