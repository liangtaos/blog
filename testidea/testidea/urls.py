"""testidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import xadmin
xadmin.autodiscover()
from django.conf.urls import url, include
from blog.views import IndexView, CategoryView, TagView, PostView,AuthorView, LinkView
from comment.views import CommentView
from testidea import adminx
from blog.api import PostViewSet, CategoryViewSet, TagViewSet, UserViewSet
from ckeditor_uploader import urls as uploader_urls
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^$',IndexView.as_view(), name='index'),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^post/(?P<pk>\d+).html',PostView.as_view(), name='post'),
    url(r'^category/(?P<category_id>\d+)/', CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_id>\d+)/',TagView.as_view(), name='tag'),
    url(r'^author/(?P<author_id>\d+)/',AuthorView.as_view(), name='author'),
    url(r'^links/$',LinkView.as_view(), name='author'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^api/', include(router.urls)),
    url(r'^api/docs/', include_docs_urls(title='My API Title'))

] + uploader_urls.urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
