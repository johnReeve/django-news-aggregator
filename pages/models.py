from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    heading = models.CharField(max_length=200)
    content = models.TextField(max_length=500)
    slug = models.SlugField(max_length=250, unique=True)
    url = models.URLField(unique=True)
    author = models.ForeignKey(User)
    published_date = models.DateTimeField(blank=True)
    submitted_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse('news_single', args=[ self.slug ])