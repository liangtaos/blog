from django.db import models
from blog.models import  Post
# Create your models here.

from django.urls import reverse
from django.utils.html import format_html

class Comment(models.Model):
    post = models.ForeignKey(Post,verbose_name='文章')
    content = models.CharField(max_length=2000,verbose_name='评论')
    nickname = models.CharField(max_length=20,verbose_name='昵称')
    website = models.URLField(blank=True,verbose_name='网站')
    email = models.EmailField(verbose_name='邮箱')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    def we(self):
        return '<a href={0}>{1}</a>'.format(self.website,self.website)

    we.short_description = 'web'

    def operator(self,obj=None):
        return format_html(
            '<a href={0}>{1}</a>'.format(self.website, self.website),)
        # reverse('cus_admin:blog_post_change',args=(obj.id,))

    operator.short_description = '网站'

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = verbose_name_plural = '评论'