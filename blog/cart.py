from decimal import Decimal
from django.conf import settings
from home.models import product as Product
from django.shortcuts import  get_object_or_404 , HttpResponse ,redirect
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        if not isinstance(product,Product):
            if product not in self.cart:
                product=get_object_or_404(Product,id=product)
                product_id= str ( product.id)
                self.cart[product_id] = {
                    'id':product_id,
                    'quantity': 0,
                    'price': str(product.price),
                    'discount': str(product.Discoust) if hasattr(product, 'Discoust') else '0'  # تخفیف به محصول اضافه می‌شود
                }
        else:
            product_id = str(product.id)
            if product_id not in self.cart:
                self.cart[product_id] = {
                    'id':product_id,
                    'quantity': 0,
                    'price': str(product.price),
                    'discount': str(product.Discoust) if hasattr(product, 'Discoust') else '0'  # تخفیف به محصول اضافه می‌شود
                }
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, productt):
        if isinstance(productt,Product):
            product_id = str(productt.id)
            if product_id in self.cart:
                del self.cart[product_id]
                self.save()
                return True
            else:
                return False
        else:
            if productt in self.cart:
                del self.cart[productt]
                self.save()
                return True
            else:
                return False

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for Productt in products:
            cart[str(Productt.id)]['product'] = Productt
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['discount'] = Decimal(item['discount'])  # تبدیل تخفیف به عدد Decimal
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def get_total_discount(self):
        """محاسبه جمع تخفیف‌های سبد خرید"""
        return sum((Decimal(item['price']) * Decimal(item['discount'])/100) * item['quantity'] for item in self.cart.values())
    def has (self , item):
        if not isinstance(item, Product):
            if item in self.cart:
                return True
            else:
                return False
    def clear(self):
        del self.session['cart']
        self.save()

    # def get_total_price(self):
    #     return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
