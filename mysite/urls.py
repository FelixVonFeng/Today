# -*- coding: UTF-8 -*-
# coding=UTF-8

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap, index
from django.contrib.sitemaps import views
from felixvon.sitemap import sitemaps
from felixvon.models import Blog, Tag
from felixvon import views
from felixvon.LatestEntriesFeed import LatestEntriesFeed

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^favicon.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
    url(r'^$', 'index', name='index'),
    url(r'^blog_detail/blog_(?P<blog_id>\d+)/$', 'blog_detail', name='blog_detail'),
    url(r'^tag_(?P<tag_id>\d+)/$', 'tag', name='tag'),
    url(r'^geek/$', 'geek', name='geek'),
    url(r'^essay/$', 'essay', name='essay'),
    url(r'^joke/$', 'joke', name='joke'),
    url(r'^profile/$', 'profile', name='profile'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^sitemap\.xml$', index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemap, {'sitemaps': sitemaps}),
    url(r'^feed/main\.xml$', LatestEntriesFeed()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)