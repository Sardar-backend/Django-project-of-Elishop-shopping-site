from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import product

class LatestEntriesFeed(Feed):
    title = "home beat site news"
    link = "/rss/feeds"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return product.objects.filter(status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
