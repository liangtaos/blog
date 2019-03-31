from django.db import models
from blog.models import  Post
# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post,verbose_name='文章')
    content = models.CharField(max_length=2000,verbose_name='评论')
    nickname = models.CharField(max_length=20,verbose_name='昵称')
    website = models.URLField(blank=True,verbose_name='网站')
    email = models.EmailField(verbose_name='邮箱')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')


    class Meta:
        verbose_name = verbose_name_plural = '评论'