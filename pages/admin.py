from django.contrib import admin
from .models import NewsItem


class NewsItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(NewsItem, NewsItemAdmin)
