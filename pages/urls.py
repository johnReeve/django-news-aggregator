from django.conf.urls import patterns, include, url

from .views import archive, single

urlpatterns = patterns('',
    url('^$', archive, name='news_archive'),
    url('^(?P<slug>[a-zA-Z0-9-]+)/$', single, name='news_single'),
)