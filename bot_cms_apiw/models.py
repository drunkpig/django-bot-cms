from django.db import models

# Create your models here.


class File(models.Model):
    """

    """
    id = models.AutoField(primary_key=True)
    belong_to_folder_id = models.ForeignKey(
        'Folder',
        on_delete=models.CASCADE,

    )  # 外键，属于那个分类

    title = models.CharField(help_text='标题',max_length=64)
    content = models.TextField(help_text="文章内容")
    template_path = models.CharField(max_length=128)  # 模版的目录

    seo_title = models.CharField(max_length=64)
    seo_keywords = models.TextField(max_length=128)
    seo_des = models.TextField(max_length=256)

    is_delete = models.BooleanField(default=False)  # 如果是True那么就会等待被删除
    is_pub = models.BooleanField(default=True)  # 是否是公开状态
    gmt_auto_pub = models.DateTimeField()  # 什么时候发布到互联网公开

    gmt_created = models.DateTimeField(auto_now_add=True)
    gmt_updated = models.DateTimeField(auto_now=True)


class Folder(models.Model):
    """

    """
    id = models.AutoField(primary_key=True)
    parent_folder_id = models.ForeignKey(
        'Folder',
        on_delete=models.CASCADE,
        null=True
    )

    name = models.CharField(max_length=32, unique=True)
    depth = models.PositiveSmallIntegerField()

    template_path = models.CharField(max_length=128)  # 模版的目录

    gmt_created = models.DateTimeField(auto_now_add=True)
    gmt_updated = models.DateTimeField(auto_now=True)
