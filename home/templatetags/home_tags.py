from django import template
from home.models import product
register = template.Library()

@register.inclusion_tag('tagstemp/p.html')
def lates_pro():
    pros = product.objects.filter(status=True).order_by('updated_date')[:3]
    return {'products':pros}
@register.inclusion_tag('tagstemp/p.html')
def lates_v():
    Product = product.objects.filter(status=True)
    Product = Product.filter(category__name="موبایل گوشی").order_by('updated_date')[:10]
    return {'products':Product}
@register.inclusion_tag('tagstemp/p.html')
def lates_s():
    Product = product.objects.filter(status=True)
    Product = Product.filter(category__name="تجهیزات جانبی گوشی").order_by('updated_date')[:7]
    return {'products':Product}
@register.inclusion_tag('tagstemp/p.html')
def lates_l():
    Product = product.objects.filter(status=True)
    Product = Product.filter(category__name="لبنیات").order_by('updated_date')[:4]
    return {'products':Product}
@register.inclusion_tag('tagstemp/p.html')
def lates_po():
    Product = product.objects.filter(status=True)
    Product = Product.filter(category__name="پروتئینی").order_by('updated_date')[:4]
    return {'products':Product}
@register.inclusion_tag('tagstemp/p.html')
def lates_r():
    Product = product.objects.filter(status=True)
    Product = Product.filter(category__name="هدفون هدست و هنذفری").order_by('updated_date')[:10]
    return {'products':Product}

@register.inclusion_tag('tagstemp/layout.html')
def profile_sidbar():
    pass
    # Product = product.objects.filter(status=True)
    # Product = Product.filter(category__name="روعن گیاهی").order_by('updated_date')[:4]
    # return {'products':Product}
