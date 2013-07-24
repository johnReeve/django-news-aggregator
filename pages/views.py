from django.http import HttpResponse
import datetime
from django.shortcuts import render, get_object_or_404

from .models import NewsItem


def archive(request):
    newsItems = NewsItem.objects.exclude(published_date__gte=datetime.date.today()).order_by('published_date').reverse()
    return render(request, 'archive.html', {'items': newsItems})


def single(request, slug):
    newsItem = get_object_or_404(NewsItem, slug=slug)
    return render(request, 'single.html', {'item': newsItem})


