from django.contrib import admin
from .models import product , comment , Category , Categorys , contact , newsletter ,adresses ,Order
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class postAdmin(SummernoteModelAdmin):
    list_filter = ('status','category',)
    summernote_fields = ('description',)
class contactAdmin(SummernoteModelAdmin):
    # list_filter = ('answer',)
    summernote_fields = ('answer',)

admin.site.register(product,postAdmin)
admin.site.register(comment)
admin.site.register(Category)
admin.site.register(Categorys)
admin.site.register(contact,contactAdmin)
admin.site.register(newsletter)
admin.site.register(adresses)
admin.site.register(Order)
