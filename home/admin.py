from django.contrib import admin
from .models import product , comment , Category  , contact  ,adresses ,Order,Color, CustomUser , ProductAttribute
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class postAdmin(SummernoteModelAdmin):
    list_filter = ('status','category',)
    summernote_fields = ('description',)
# class contactAdmin(SummernoteModelAdmin):
#     # list_filter = ('answer',)
#     summernote_fields = ('answer',)

class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductAttributeInline]

admin.site.register(product, ProductAdmin)

# admin.site.register(product,postAdmin)
admin.site.register(comment)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(CustomUser)

admin.site.register(contact)

admin.site.register(adresses)
admin.site.register(Order)
