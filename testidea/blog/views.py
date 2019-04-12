# Create your views here.

from .models import Post,Tag, Category
from config.models import Link, SideBar
from comment.models import Comment

from django.views.generic import ListView  # 对多个对象展示的应用，列表展示
from django.views.generic import DetailView # 对单个对象展示的应用


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

        hotPosts = Post.objects.all()[:10]
        sidebar = SideBar.objects.all().order_by('display_type')
        comment = Comment.objects.all().order_by('created_time')[:5]
        extra_context = {
            'showCate': showCate,
            'hiddenCate': hiddenCate,
            'hotPosts': hotPosts,
            'sidebar': sidebar,
            'comment': comment,
        }
        context = super(CommonMixin, self).get_context_data(**kwargs)
        context.update(extra_context)
        return context


class BasePostView(CommonMixin, ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'posts'
    paginate_by = 4

    # def get_context_data(self, **kwargs):
    #     cates = Category.objects.all()
    #     showCate = []
    #     hiddenCate = []
    #     for cate in cates:
    #         if cate.is_nav:
    #             showCate.append(cate)
    #         else:
    #             hiddenCate.append(cate)
    #     context = super(BasePostView, self).get_context_data(**kwargs)
    #     hotPosts = Post.objects.all()[:10]
    #     sidebar = SideBar.objects.all().order_by('display_type')
    #     comment = Comment.objects.all().order_by('created_time')[:5]
    #     extra_context = {
    #         'showCate': showCate,
    #         'hiddenCate': hiddenCate,
    #         'hotPosts': hotPosts,
    #         'sidebar': sidebar,
    #         'comment': comment,
    #     }
    #     context.update(extra_context)
    #     return context


class IndexView(BasePostView):
    pass


class CategoryView(BasePostView):
    def get_queryset(self):
        qs = super(CategoryView,self).get_queryset()
        cate_id = self.kwargs.get('category_id')
        qs = qs.filter(category_id=cate_id)
        return qs


class TagView(BasePostView):
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
    template_name = 'detail.html'
    context_object_name = 'post'

