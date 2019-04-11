from django.contrib import admin
# Register your models here.
from django.http import HttpResponse
from .models import Comment
from testidea.custom_site import custom_site

from django.utils.html import format_html
from django.urls import reverse



@admin.register(Comment,site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'operator','post', 'email', 'created_time', ]
    # list_display_links = ('website',)



# admin.site.register(Comment, CommentAdmin)