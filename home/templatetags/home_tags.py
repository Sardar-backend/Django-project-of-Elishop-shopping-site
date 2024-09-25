from django import template
from home.models import product
from blog.cart import Cart
register = template.Library()
@register.filter
def range_filter(y):
    return range(5)

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
    Product = product.objects.filter(status=True).order_by('-counted_view')[:10]
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

@register.inclusion_tag('tagstemp/cart.html')
def cart_fotter():
    cart = request.session.cart
    return {'cart': cart}

@register.simple_tag(takes_context=True)
def get_user_info(context):
    request = context['request']
    user = request.user
    return f"User: {user.username}" if user.is_authenticated else "Guest"

@register.filter
def range_filter(value):
    return range(value)
@register.filter
def range_dfilter(value):
    return range( 5 - value )
@register.filter
def first_three_words(value):
    words = value.split()
    return ' '.join(words[:3])
# @register.filter
# def index_of(value, arg):
#     try:
#         return value.index(arg)
#     except ValueError:
#         return -1
@register.simple_tag
def multiply(value1, value2):
    return value1 * ( 100 - value2)/100
