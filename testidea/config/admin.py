from django.contrib import admin

# Register your models here.


from .models import SideBar, Link
from testidea.custom_site import custom_site


@admin.register(SideBar,site=custom_site)
class SideBarAdmin(admin.ModelAdmin):
    pass


@admin.register(Link, site=custom_site)
class LinkAdmin(admin.ModelAdmin):
    pass


# admin.site.register(SideBar,SideBarAdmin)
# admin.site.register(Link,LinkAdmin)
