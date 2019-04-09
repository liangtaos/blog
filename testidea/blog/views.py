from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Post,Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request, category_id=None, tag_id=None):
    queryset = Post.objects.all()
    page_size = 3
    if category_id:
        queryset = queryset.filter(category_id=category_id)
    elif tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Exception as e:
            return HttpResponse(404)
        queryset = tag.tags.all()
    if not queryset:
        return HttpResponse(404)

    paginator = Paginator(queryset, page_size)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        queryset = paginator.page(currentPage)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'posts': queryset,
        'page': currentPage
    }

    return render(request, 'list.html', context=context,)



def detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Exception as DoesNotExist:
        return HttpResponse(404)
    context = {
        'post': post
    }

    return render(request, 'detail.html', context=context)