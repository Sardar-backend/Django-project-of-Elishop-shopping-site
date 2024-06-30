from django.contrib.sitemaps import Sitemap
from home.models import product

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return product.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.updated_date
