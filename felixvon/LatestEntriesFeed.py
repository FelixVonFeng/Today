# -*- coding:utf8 -*-
from django.contrib.syndication.views import Feed
from felixvon.models import Blog


class LatestEntriesFeed(Feed):
    title = u"Felix Von"
    link = "fengjixuan.com"
    description = "Follow Felix Von Right Now!!!"

    def items(self):
        return Blog.objects.order_by('-pub_time')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return "/blog_detail/blog_" + str(item.id)
