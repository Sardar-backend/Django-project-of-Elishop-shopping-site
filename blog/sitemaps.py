from django.contrib.sitemaps import Sitemap
from home.models import product  ,Category

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return product.objects.filter(status=True)

    def items(self):
        return product.objects.filter(status=True)

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.created_date
