# coding:utf-8

from django.db import models

# Create your models here.


# 用来修改admin中显示的app名称
class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self


STATUS = {
    0: u'正常',
    1: u'草稿',
    2: u'删除',
}


# 圈子
class Zone(models.Model):
    # 基本信息
    name = models.CharField(max_length=40, verbose_name=u'圈子')
    summary = models.TextField(verbose_name=u'圈子简介')
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name=u'状态')
    post_count = models.IntegerField(default=0, verbose_name=u'帖子数目')

    # 外键-->圈友
    user = models.ManyToManyField(User, verbose_name=u'圈友')

    class Meta:
        verbose_name_plural = verbose_name = u'圈子'
        ordering = ['-post_count']
        app_label = string_with_title('club', u'圈子管理')

    def __unicode__(self):
        return self.title


# 帖子在数据库的存储
class Post(models.Model):

    # 外键:主题帖
    zone = models.ForeignKey(Zone, verbose_name=u'所属圈子')
    user = models.ForeignKey(User, verbose_name=u'发布者')

    # 基本信息，不是外键的
    name = models.CharField(max_length=40, verbose_name=u'发布者')
    title = models.ForeignKey(max_length=100, verbose_name=u'标题')
    summary = models.TextField(verbose_name=u'摘要')
    content = models.TextField(verbose_name=u'正文')
    image = models.CharField(max_length=200)  # 此处应该限制用户上传图片数量

    view_times = models.IntegerField(default=0, verbose_name=u'查看次数')
    comment_times = models.IntegerField(default=0, verbose_name=u'回帖次数')
    zan_times = models.IntegerField(default=0, verbose_name=u'点赞人数')

    pub_time = models.DateTimeField(default=False, verbose_name=u'发布时间')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name=u'状态')

    class Meta:
        verbose_name_plural = verbose_name = u'帖子'
        ordering = ['-pub_time', '-create_time']
        app_label = string_with_title('club', u'圈子管理')

    def __unicode__(self):
        return self.title


# TODO:默认用户头像，找一些漂亮的 ||Django验证系统，auth，字段要求！！！
# 面向用户的，一些信息对管理员不可见
class User(models.Model):

    # 基本信息
    name = models.CharField(max_length=40, verbose_name=u'头像')
    birthday = models.DateField(verbose_name=u'生日')
    img = models.CharField(max_length=200, default='/static/...', verbose_name=u'头像地址')
    intro = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'简介')

    # 安全信息
    email = models.EmailField(verbose_name=u'邮箱地址')

    # 关注了谁，谁关注了你(自我递归的多对多关系)
    stars = models.ManyToManyField('self')
    fans = models.ManyToManyField('self')

    class Meta:
        verbose_name_plural = verbose_name = u'用户信息'
        app_label = string_with_title('club', u'用户信息管理')

    def __unicode__(self):
        return self.title


# 记录帖子情况,两个外键是为了跟踪用户最近操作与帖子跟帖数目
class Comment(models.Model):

    # 基本信息
    content = models.TextField(verbose_name=u'回帖内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'回复时间')

    # 回复人
    commenter = models.ForeignKey(User, verbose_name=u'跟帖人')
    # 主题帖
    post = models.ForeignKey(Post, verbose_name=u'主题帖')

    class Meta:
        verbose_name_plural = verbose_name = u'回复帖子'
        app_label = string_with_title('club', u'回复帖子管理')

    def __unicode__(self):
        return self.title







