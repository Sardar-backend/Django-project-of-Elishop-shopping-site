from django.shortcuts import render ,get_list_or_404
from home.models import product
from home.models import comment
from home.form import commentform
from django.contrib import messages
from django.views.generic import TemplateView , ListView
# Create your views here.


def product_view(request,pid):
    if request.method == 'POST':
        form = commentform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'کامنت شما با موفقیت ارسال شد')
        else:
            messages.add_message(request,messages.ERROR,'متاسفانه کامنت شما ارسال نشد')
    # Product = product.objects.filter(status=True)
    p = get_list_or_404(product,pk=pid,status=True)
    # comments = get_list_or_404(comment,pro=pid,status=True)
    comments =comment.objects.filter(pro=pid,status=True)
    context = {'products':p ,'comments':comments}
    return render(request, 'blog/product.html',context)

def search_view (request):
    Product = product.objects.filter(status=True)
    if request.method == 'GET':
        Product = Product.filter(description__contains =request.GET.get('p'))
    # req =request.GET.get('p')
    context = {'products':Product }
    return render(request, 'view/products.html',context)

class limit_view (ListView):
    queryset = product.objects.filter(status=True,Discoust__gt=40).order_by('-Discoust')
    template_name = 'view/products.html'
    paginate_by = 12
    context_object_name= 'products'
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
    return render(request, 'view/products.html',context)
# ,'req':req


# def limit_view (request):
#     Product = product.objects.filter(status=True,Discoust__lte=70).order_by('-Discoust')
#     context = {'products':Product}
#     return render(request, 'blog/off.html',context)
