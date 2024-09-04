from typing import Any
from django.shortcuts import render , HttpResponseRedirect
from home.models import product , adresses
from home.models import Categorys , Category
from django.core.paginator import Paginator
from home.form import contactform , neeslettertform ,adressform
from django.contrib import messages
from django.views.generic import TemplateView , ListView

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'پیام شما با موفقیت ارسال شد')
        else:
            messages.add_message(request,messages.ERROR,'متاسفانه پیام شما ارسال نشد')
    form = contactform()
    return render(request, 'view/profile/add-ticket.html',{'form':form})
def add_adress(request):
    if request.method == 'POST':
        form = adressform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'پیام شما با موفقیت ارسال شد')
        else:
            messages.add_message(request,messages.ERROR,'متاسفانه پیام شما ارسال نشد')
    form = adressform()
    return render(request, 'view/profile/add-adress.html',{'form':form})
class category_view(TemplateView):
    template_name = 'view/category.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        category = Category.objects.all()
        context['categorys'] = list(category)
        return context

class products_view(ListView):
    template_name = 'view/products.html'
    queryset = product.objects.filter(status=True)
    ordering = 'created_date'
    # ordering = '-created_date'
    paginate_by = 12
    context_object_name= 'products'


class products_exist (ListView):
    template_name = 'view/products.html'
    queryset = product.objects.filter(status=True,count__gt=0)
    ordering = 'created_date'
    # ordering = '-created_date'
    paginate_by = 12
    context_object_name= 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exist'] = 'فقط کالا های موجود'
        # context["now"] = timezone.now()
        return context

class products_ready(ListView):
    template_name = 'view/products'
    queryset = product.objects.filter(status=True,Ready_to_send= True)
    ordering = 'created_date'
    paginate_by = 12
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['exist'] = 'فقط کالا های آماده ارسال'
        return context


def products_views(request,cat_name):
    Product = product.objects.filter(status=True)
    x= Product.filter(category__name=cat_name)
    x = Paginator(x,12)
    page_number = request.GET.get('page')
    x = x.get_page(page_number)
    context = {'products':x}
    return render(request, 'view/products.html',context)


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

def profile(request):
    #item= adresses.objects.filter(user=request.user.id)
    item= adresses.objects.all()
    x=item.count()
    ite = [1,2,3,4,5,6,7,8,9]
    context = {'adress':ite,
               x:'x'}
    return render(request, 'view/profile/profile.html', context)
# def add_adress(request):
#     return render(request, 'view/profile/add-adress.html')

def edit_personal(request):
    return render(request, 'view/profile/edit-personal-info.html')

def favorates(request):
    return render(request, 'view/profile/favorates.html')


def list_ticket(request):
    return render(request, 'view/profile/ticket.html')

def product_orders(request):
    return render(request, 'view/profile/product-orders.html')

def notifications(request):
    return render(request, 'view/profile/notification.html')


class about (TemplateView):
    template_name = 'view/about.html'


class home_view (TemplateView):
    template_name = 'view/index.html'

    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)

# def about(request):
#     return render(request, 'view/about.html')

# def home_view(request):
#     return render(request, 'view/index.html')

# def category_view(request):
#     # category = Categorys.objects.all()
#     category = Category.objects.all()
#     text = {'categorys':list(category)}
#     return render(request, 'view/category.html', text)
# def products_view(request):
#     Product = product.objects.filter(status=True)
#     Product = Paginator(Product,12)
#     page_number = request.GET.get('page')
#     Product = Product.get_page(page_number)
#     context = {'products':Product}
#     return render(request, 'view/products.html',context )

# def products_exist(request):
#     Product = product.objects.filter(status=True,count__gt=0)
#     Product = Paginator(Product,12)
#     page_number = request.GET.get('page')
#     Product = Product.get_page(page_number)
#     context = {'products':Product,
#                'exist':'فقط کالا های موجود'}
#     return render(request, 'view/products.html',context )
# def products_ready(request):
#     Product = product.objects.filter(status=True,Ready_to_send=True)
#     Product = Paginator(Product,12)
#     page_number = request.GET.get('page')
#     Product = Product.get_page(page_number)
#     context = {'products':Product,
#                'exist':'فقط کالا های آماده ارسال'}
#     return render(request, 'view/products.html',context )
