from django.shortcuts import render , HttpResponseRedirect
from home.models import product
from home.models import Categorys
from django.core.paginator import Paginator
from home.form import contactform , neeslettertform
from django.contrib import messages
# Create your views here.
def home_view(request):
    return render(request, 'view/index.html')
def contact_view(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'پیام شما با موفقیت ارسال شد')
        else:
            messages.add_message(request,messages.ERROR,'متاسفانه پیام شما ارسال نشد')
    form = contactform()
    return render(request, 'view/contact.html',{'form':form})
def category_view(request):
    category = Categorys.objects.all()
    text = {'categorys':category}
    return render(request, 'view/category.html', text)
def products_view(request):
    Product = product.objects.filter(status=True)
    Product = Paginator(Product,8)
    page_number = request.GET.get('page')
    Product = Product.get_page(page_number)
    context = {'products':Product}
    return render(request, 'view/products.html',context)

def products_views(request,cat_name):
    Product = product.objects.filter(status=True)
    x= Product.filter(category__name=cat_name)
    x = Paginator(x,8)
    page_number = request.GET.get('page')
    x = x.get_page(page_number)
    context = {'products':x}
    return render(request, 'view/pros.html',context)
# def products (request,name):
#     Productss = product.objects.filter(status=True)
#     xx= Productss.filter(category__name=name)
#     contextt = {'products':xx}
#     return render(request, 'view/prose.html',contextt)
def newsletter(request):
    if request.method == 'POST':
        form = neeslettertform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
