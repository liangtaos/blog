from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True,verbose_name = '标题')