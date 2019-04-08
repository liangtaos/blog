from django.contrib import admin

# Register your models here.


from .models import Comment
from testidea.custom_site import custom_site

@admin.register(Comment,site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Comment, CommentAdmin)