from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Post, Tag, Category, TopNav
from config.models import Link, SideBar
from comment.models import Comment
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic import DetailView
from django.db.models import Q
from comment.forms import CommentForm


class CommonMixin(object):
    def get_context_data(self, **kwargs):
        cates = Category.objects.all()
        showCate = []
        hiddenCate = []
        for cate in cates:
            if cate.is_nav:
                showCate.append(cate)
            else:
                hiddenCate.append(cate)
        context = super(CommonMixin, self).get_context_data(**kwargs)
        hotPosts = Post.objects.all()[:10]
        sidebar = SideBar.objects.all().order_by('display_type')
        comment = Comment.objects.all().order_by('created_time')[:5]
        nav = TopNav.objects.filter(status=1)
        url_ = self.request.path
        extra_context = {
            'url': url_,
            'navs': nav,
            'showCate': showCate,
            'hiddenCate': hiddenCate,
            'hotPosts': hotPosts,
            'sidebar': sidebar,
            'comment': comment,
        }
        context.update(extra_context)
        return context


class BasePostView(CommonMixin, ListView,):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 10






class IndexView(BasePostView):
    def get_queryset(self):
        qs = super(IndexView, self).get_queryset()
        query = self.request.GET.get('query')
        if not query:
            return qs
        return qs.filter(Q(title__icontains=query)|Q(category__name__icontains=query)|Q(owner__username__icontains=query)|Q(tag__name__icontains=query))

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        return super(IndexView, self).get_context_data(query=query)


class AuthorView(BasePostView):
    def get_queryset(self):
        author_id = self.kwargs.get('author_id')
        qs = super(AuthorView, self).get_queryset()
        if author_id:
            qs = qs.filter(owner=author_id)
        return qs


class CategoryView(BasePostView):
    def get_queryset(self):
        qs = super(CategoryView,self).get_queryset()
        cate_id = self.kwargs.get('category_id')
        qs = qs.filter(category_id=cate_id)
        return qs

class LinkView(BasePostView, ListView):
    model = Link
    template_name = 'blog/links.html'
    context_object_name = 'links'

    def get_queryset(self):
        qs = Link.objects.filter(status=1).order_by('-weight')
        return qs


class TagView(BasePostView):

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({'tag': tag})
        return context

    def get_queryset(self):
        tag_id = self.kwargs.get('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return []
        posts = tag.tags.all()
        return posts

class PostView(CommonMixin,DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        kwargs.update({
            'comment_form': CommentForm(),
        })
        return super(PostView, self).get_context_data(**kwargs)
