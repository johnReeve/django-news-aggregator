import datetime
from django import template
from ..models import NewsItem

register = template.Library()


@register.inclusion_tag('newsItem_list_snippet.html', takes_context=True)
def most_recent_news(context, count):
    items = newsItems = NewsItem.objects.exclude(published_date__gte=datetime.date.today()).order_by('published_date').reverse()[:count]
    return {'items': items}


