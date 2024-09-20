from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home:index','home:category_view','home:contact_view','home:faq','home:products_view','home:cheapest','home:expensive','home:discounts','home:exist','home:ready','home:profile','home:profile_add_adress','home:favorates','home:list_ticket','home:product-orders','home:about','home:privacy','blog:search','blog:filter','blog:limit','blog:cart_detail']

    def location(self, item):
        return reverse(item)
