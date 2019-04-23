from django.contrib import admin
# Register your models here.
from django.http import HttpResponse
from .models import Comment

import xadmin


# @admin.register(Comment,site=custom_site)
class CommentAdmin(object):
    list_display = ['nickname', 'operator','target', 'email', 'created_time', ]
    # list_display_links = ('website',)



xadmin.site.register(Comment, CommentAdmin)