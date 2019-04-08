from django.contrib import admin

# Register your models here.

from testidea.BaseAdmin import BaseOwnerAdmin

from .models import SideBar, Link
from testidea.custom_site import custom_site


@admin.register(SideBar,site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ['title', 'owner', 'created_time', 'status_type']


@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ['title', 'href', 'owner', 'created_time']
    list_display_links = ('href',)


# admin.site.register(SideBar,SideBarAdmin)
# admin.site.register(Link,LinkAdmin)
