from __future__ import unicode_literals

# Create your models here.

from django.db import models
from DjangoUeditor.models import UEditorField

import sys

reload(sys)
sys.setdefaultencoding('utf8')


class Category1(models.Model):
    category_1 = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.category_1

    class Meta:
        ordering = ['-add_time']


class Category2(models.Model):
    category_2 = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.category_2

    class Meta:
        ordering = ['-add_time']


class Tag(models.Model):
    tag = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag

    class Meta:
        ordering = ['-add_time']


class Blog(models.Model):
    title = models.CharField(u'Title', max_length=100)
    head_pic_url = models.CharField(u'Head_pic_url', max_length=250, default='/static/img/default.jpg')
    pub_time = models.DateTimeField(auto_now_add=True)
    brief = models.CharField(u'Brief', max_length=200, blank=True, null=True)
    content = UEditorField(u'Content', width=900, height=600, toolbars="full", imagePath="", settings={})
    page_views = models.PositiveIntegerField(u'Page_views', default=0, editable=False)
    category1 = models.ForeignKey(Category1, verbose_name=u'Category1')
    category2 = models.ForeignKey(Category2, null=True, verbose_name=u'Category2')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'Tags')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-pub_time']


class Profile_Tag(models.Model):
    tag = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag

    class Meta:
        ordering = ['-add_time']


class Profile(models.Model):
    title = models.CharField(u'Title', max_length=100)
    head_pic_url = models.CharField(u'Head_pic_url', max_length=250, default='/static/img/default.jpg', null=True, blank        =True)
    pub_time = models.DateTimeField(auto_now_add=True)
    content = UEditorField(u'Content', width=900, height=600, toolbars="full", imagePath="", settings={})
    tags = models.ManyToManyField(Profile_Tag, blank=True, verbose_name=u'Tags')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-pub_time']


class Friend_Tag(models.Model):
    tag = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag

    class Meta:
        ordering = ['-add_time']


class Friend(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True)
    friend_url = models.CharField(u'Url', max_length=250, default='http://')
    tags = models.ManyToManyField(Friend_Tag, blank=True, verbose_name=u'Tags')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

