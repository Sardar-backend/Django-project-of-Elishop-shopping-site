from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home:prose', 'home:products_view' , 'home:category_view','home:contact_view','home:blog_view','blog:search','blog:login_view']

    def location(self, item):
        return reverse(item)
