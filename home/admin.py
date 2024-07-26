from django.contrib import admin
from .models import product , comment , Category , Categorys , contact , newsletter
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class postAdmin(SummernoteModelAdmin):
    list_filter = ('status','category',)
    summernote_fields = ('description',)
admin.site.register(product,postAdmin)
admin.site.register(comment)
admin.site.register(Category)
admin.site.register(Categorys)
admin.site.register(contact)
admin.site.register(newsletter)

