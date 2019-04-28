from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import markdown

class Category(models.Model):
    STATUS_ITEMS = (
        (1,'可用'),
        (2,'删除'),
    )

    name = models.CharField(max_length=50,verbose_name='名称')   #
    status = models.PositiveIntegerField(default=1,choices=STATUS_ITEMS,verbose_name='状态')
    is_nav = models.BooleanField(default=True,verbose_name='是否为导航')
    owner = models.ForeignKey(User,verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:    #后台的显示名称
        verbose_name = verbose_name_plural = '分类'

class Tag(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )

    name = models.CharField(max_length=10, verbose_name="名称")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")

    owner = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '标签'


class Post(models.Model):
    STATUS = (
        (1, '上线'),
        (2,'草稿'),
        (3,'删除'),
    )
    title = models.CharField(max_length=50,verbose_name='标题')  #blank=True  可以为空字段
    desc = models.CharField(max_length=255, blank=True, verbose_name='摘要')
    category = models.ForeignKey(Category, verbose_name='分类')
    tag = models.ManyToManyField(Tag,verbose_name='标签',related_name='posts')
    content = models.TextField(verbose_name='内容', help_text="注:目前仅支持Markdown格式")
    is_markdown = models.BooleanField(default=False, verbose_name='支持Markdown格式')
    html = models.TextField(default='', verbose_name='渲染后的内容')
    status = models.IntegerField(default=1,choices=STATUS,verbose_name='状态')
    pv = models.IntegerField(default=0, verbose_name='阅读量')
    uv = models.IntegerField(default=0, verbose_name='日用户量')
    img_src = models.ImageField(upload_to='Isrc', blank=True, verbose_name='图片路径')
    owner = models.ForeignKey(User,verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')##增加文章则自动添加时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')  # 修改自动添加时间


    def prev_post(self):
        return Post.objects.filter(id__lt=self.id).first()


    def next_post(self):
        return Post.objects.filter(id__gt=self.id).order_by('id').first()

    def img_url(self):
        import pdb; pdb.set_trace()
        return


    def status_show(self):
        return '当前状态: %s'% (dict(self.STATUS)[self.status])

    status_show.short_description = '展示状态'

    def save(self, *args, **kwargs):
        if self.is_markdown:
            config = {
                'codehilite': {
                    'use_pygments': False,
                    'css_class': 'prettyprint linenums',
                }
            }
            self.html = markdown.markdown(self.content, extensions=["codehilite"], extension_configs=config)
        else:
            self.html = self.content

        return super(Post, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-created_time', '-id']


class TopNav(models.Model):
    STATUS = (
        (1, '正常'),
        (2, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name='名字')
    url = models.URLField(verbose_name='链接')
    owner = models.ForeignKey(User, verbose_name='作者')
    status = models.IntegerField(default=1,choices=STATUS,verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '顶部导航'