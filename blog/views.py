from django.shortcuts import render ,get_list_or_404 ,HttpResponse,get_object_or_404 ,redirect
from home.models import product ,adresses ,comment ,Color
from home.form import commentform
from django.contrib import messages
from django.views.generic import TemplateView , ListView
from django.db.models import Q
from .cart import Cart
from django.http import FileResponse
import os

# Create your views here.


def product_view(request,pid):
    if request.method == 'POST':
        form = commentform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'کامنت شما با موفقیت ارسال شد')
        else:
            messages.add_message(request,messages.ERROR,'متاسفانه کامنت شما ارسال نشد')
    p =get_object_or_404 (product,pk=pid,status=True)
    price = p.price * (p.Discoust)/100
    c= product.objects.filter(id=pid)
    favorates= product.objects.filter(favorites__id=request.user.id)
    color= Color.objects.filter(product__id=p.id)
    comments =comment.objects.filter(pro=pid,status=True)


    lencomments = len(comments) if len(comments)!=0 else 1
    v=c[0].counted_view +1
    product.objects.filter(id=pid).update(counted_view=v)
    context = {'p':p ,'comments':comments,'favorates':favorates,'price':price}
    cart =Cart(request)
    context['CartNumber'] =len(cart)
    context['colorlist']=color
    context['Cart'] =cart
    context['total'] =cart.get_total_price()
    context['average_cost'] =sum(item.cost for item in comments) /lencomments
    context['average_Quality'] =sum(item.quality for item in comments) /lencomments
    context['average_Innovation'] =sum(item.Innovation for item in comments) /lencomments
    context['average_Beauty'] =sum(item.beauty for item in comments) /lencomments
    context['average_Longevity'] =sum(item.Longevity for item in comments) /lencomments
    context['average_Services'] =sum(item.Services for item in comments) /lencomments
    context['product_url'] =  request.build_absolute_uri()
    return render(request, 'blog/product.html',context)

def search_view (request):
    # Product = product.objects.filter(status=True)
    if request.method == 'GET':
        #Product = Product.filter(Q(description__contains =request.GET.get('p') | brand =request.GET.get('p')))
        z= request.GET.get('p')
        Product = product.objects.filter(Q(title=z) | Q(description__contains=z) | Q(brand=z) , status=True )
        # Product = Product.objects.filter(status=True)
    # req =request.GET.get('p')
    context = {'products':Product }
    cart =Cart(request)
    context['CartNumber'] =len(cart)
    context['Cart'] =cart
    context['total'] =cart.get_total_price()
    return render(request, 'view/products.html',context)

class limit_view (ListView):
    queryset = product.objects.filter(status=True,Discoust__gt=40).order_by('-Discoust')
    template_name = 'view/products.html'
    paginate_by = 12
    context_object_name= 'products'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        cart =Cart(self.request)
        context['CartNumber'] =len(cart)
        context['Cart'] =cart
        context['total'] =cart.get_total_price()

        return context
# def limit_vip (request):
#     Product = product.objects.filter(status=True,Discoust__lte=45).order_by('-Discoust')
#     context = {'products':Product}
#     return render(request, 'blog/off.html',context)

def range_view (request):
    Product = product.objects.filter(status=True)
    if request.method == 'GET':
        Product = Product.filter(price__range=(int(request.GET.get('min_price')), request.GET.get('max_price')))
    # req =request.GET.get('p')
    context = {'products':Product }
    cart =Cart(request)
    context['CartNumber'] =len(cart)
    context['Cart'] =cart
    context['total'] =cart.get_total_price()
    return render(request, 'view/products.html',context)

def delete_favorates (request,pid):
    if request.method == 'POST':
        p=get_object_or_404(product,pk=pid)
        p.favorites.remove(request.user)
        return redirect(request.META.get('HTTP_REFERER'))

def delete_adresses (request,pid):
    if request.method == 'POST':
        adresse=get_object_or_404(adresses,pk=pid)
        adresse.delete()
        return redirect(request.META.get('HTTP_REFERER'))


def download_file(request):
    file_path = os.path.join('medias', 'MyResume-314[www.cvbuilder.me].pdf')  # مسیر به پوشه‌ی فایل‌ها
    return FileResponse(open(file_path, 'rb'))





def add_to_cart(request, product_id):
    cart = Cart(request)
    Product = get_object_or_404(product, id=product_id)
    cart.add(product=Product)
    return redirect(request.META.get('HTTP_REFERER'))

def remove_from_cart(request, product_id):
    cart = Cart(request)
    Product = get_object_or_404(product, id=product_id)
    cart.remove(Product)
    return redirect(request.META.get('HTTP_REFERER'))

def cart_detail(request):
    cart = Cart(request)
    context ={'cart': cart}
    context['CartNumber'] =len(cart)
    context['Cart'] =cart
    context['total'] =cart.get_total_price()
    context['totalDiscount'] =cart.get_total_discount()
    context['finalPrice'] = cart.get_total_price() - cart.get_total_discount()
    if len(cart):
        return render(request, 'Cart/mycart.html', context)
    return render(request, 'Cart/mycartEmpty.html', context)
