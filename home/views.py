from typing import Any
from django.shortcuts import render , HttpResponseRedirect , HttpResponse ,get_object_or_404 ,redirect
from home.models import product , adresses
from home.models import  Category , contact
from django.core.paginator import Paginator
from home.form import contactform  ,adressform , captcha , Userform
from django.contrib import messages
from django.views.generic import TemplateView , ListView
from django.contrib.auth.decorators import login_required
from blog.cart import Cart
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
# Create your views here.
@login_required(login_url='/accounts/login')
def contact_view(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'تیکت  شما با موفقیت ارسال شد و بزودی پاسخ داده خواهد شد' )
            # messages.add_message(request,messages.SUCCESS,'پیام شما با موفقیت ارسال شد')
        else:
            messages.error(request,'متاسفانه پیام شما ارسال نشد لطفا دوباره تلاش کنید')
            # messages.add_message(request,messages.ERROR,'متاسفانه پیام شما ارسال نشد')
    form = contactform()
    username=request.user.id
    context ={'form':form,'username':username}
    cart =Cart(request)
    context['CartNumber'] =len(cart)
    context['Cart'] =cart
    context['total'] =cart.get_total_price()
    return render(request, 'view/profile/add-ticket.html',context)

@login_required(login_url='/accounts/login')
def add_adress(request):
    if request.method == 'POST':
        form = adressform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'ادرس  شما با موفقیت ثبت شد و بزودی پاسخ داده خواهد شد')
            # messages.add_message(request,messages.SUCCESS,'پیام شما با موفقیت ارسال شد')
        else:
            messages.error(request,'متاسفانه ادرس شما ثبت نشد لطفا دوباره تلاش کنید')
            #messages.add_message(request,messages.ERROR,'متاسفانه پیام شما ارسال نشد')
    form = adressform()
    context ={'form':form}
    cart =Cart(request)
    context['CartNumber'] =len(cart)
    context['Cart'] =cart
    context['total'] =cart.get_total_price()
    return render(request, 'view/profile/add-adress.html',context)

class category_view(TemplateView):
    template_name = 'view/category.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        category = Category.objects.all()
        context['categorys'] = list(category)
        context['Categorys'] = list(category)[5:]
        cart =Cart(self.request)
        context['CartNumber'] =len(cart)
        context['Cart'] =cart
        context['total'] =cart.get_total_price()
        return context


class products_view(ListView):
    template_name = 'view/products.html'
    queryset = product.objects.filter(status=True)
    ordering = 'created_date'
    # ordering = '-created_date'
    paginate_by = 12
    context_object_name= 'products'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        cart =Cart(self.request)
        context['CartNumber'] =len(cart)
        context['Cart'] =cart
        context['total'] =cart.get_total_price()
        return context


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
        cart =Cart(self.request)
        context['CartNumber'] =len(cart)
        context['Cart'] =cart
        context['total'] =cart.get_total_price()
        return context

class cheapest (ListView):
    template_name = 'view/products.html'
    queryset = product.objects.filter(status=True)
    ordering = 'price'
    # ordering = '-created_date'
    paginate_by = 12
    context_object_name= 'products'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        cart =Cart(self.request)
        context['CartNumber'] =len(cart)
        context['Cart'] =cart
        context['total'] =cart.get_total_price()
        return context

class expensive (ListView):
    template_name = 'view/products.html'
    queryset = product.objects.filter(status=True)
    ordering = '-price'
    # ordering = '-created_date'
    paginate_by = 12
    context_object_name= 'products'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        cart =Cart(self.request)
        context['CartNumber'] =len(cart)
        context['Cart'] =cart
        context['total'] =cart.get_total_price()
        return context

class discounts (ListView):
    template_name = 'view/products.html'
    queryset = product.objects.filter(status=True)
    ordering = '-Discoust'
    # ordering = '-created_date'
    paginate_by = 12
    context_object_name= 'products'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        cart =Cart(self.request)
        context['CartNumber'] =len(cart)
        context['Cart'] =cart
        context['total'] =cart.get_total_price()
        return context


class products_ready(ListView):
    template_name = 'view/products.html'
    queryset = product.objects.filter(status=True,Ready_to_send= True)
    ordering = 'created_date'
    paginate_by = 12
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        cart =Cart(self.request)
        context['CartNumber'] =len(cart)
        context['Cart'] =cart
        context['total'] =cart.get_total_price()
        context['exist'] = 'فقط کالا های آماده ارسال'
        return context

    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     cart =Cart(self.request)
    #     context['CartNumber'] =len(cart)
    #     context['Cart'] =cart
    #     context['total'] =cart.get_total_price()
    #     return context

def products_views(request,cat_name):
    Product = product.objects.filter(status=True)
    x= Product.filter(category__name=cat_name)
    x = Paginator(x,12)
    page_number = request.GET.get('page')
    x = x.get_page(page_number)
    context = {'products':x}
    cart =Cart(request)
    context['CartNumber'] =len(cart)
    context['Cart'] =cart
    context['total'] =cart.get_total_price()
    return render(request, 'view/products.html',context)


# def products (request,name):
#     Productss = product.objects.filter(status=True)
#     xx= Productss.filter(category__name=name)
#     contextt = {'products':xx}
#     return render(request, 'view/prose.html',contextt)





@login_required(login_url='/accounts/login')
def profile(request):
    item= adresses.objects.filter(user=request.user.id)
    # item= adresses.objects.all()
    x=item.count()
    # ite = [1,2,3,4,5,6,7,8,9]
    context = {'adress':item,'x':x}
    cart =Cart(request)
    context['CartNumber'] =len(cart)
    context['Cart'] =cart
    context['total'] =cart.get_total_price()
    return render(request, 'view/profile/profile.html', context)
# def add_adress(request):
#     return render(request, 'view/profile/add-adress.html')
@login_required(login_url='/accounts/login')
def edit_personal(request):
    if request.method == 'POST':
        form = Userform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home:index')
        return HttpResponse('no')
    return render(request, 'view/profile/edit-personal-info.html')
@login_required(login_url='/accounts/login')
def favorates(request):
    if request.method == 'POST':
        #p=product.objects.filter(id=request.POST.get('product_id'))
        p=get_object_or_404(product,pk=request.POST.get('product_id'))
        request.user.favorites.add(p)
        return redirect(request.META.get('HTTP_REFERER'))
    favorates= request.user.favorites.all()
    context= {'favorates':favorates}
    cart =Cart(request)
    context['CartNumber'] =len(cart)
    context['Cart'] =cart
    context['total'] =cart.get_total_price()
    return render(request, 'view/profile/favorates.html', context)

@login_required(login_url='/accounts/login')
def list_ticket(request):
    tickets= contact.objects.filter(name=request.user.id)
    context= {'tickets':tickets}
    cart =Cart(request)
    context['CartNumber'] =len(cart)
    context['Cart'] =cart
    context['total'] =cart.get_total_price()
    return render(request, 'view/profile/ticket.html',context)

@login_required(login_url='/accounts/login')
def product_orders(request):
    context= {}
    cart =Cart(request)
    context['CartNumber'] =len(cart)
    context['Cart'] =cart
    context['total'] =cart.get_total_price()
    return render(request, 'view/profile/product-orders.html',context)



def comment (request,id):
    x = get_object_or_404(product,id=id,status=True)
    t= request.user
    context = {'product':x,'t':t}
    cart =Cart(request)
    context['CartNumber'] =len(cart)
    context['Cart'] =cart
    context['total'] =cart.get_total_price()
    return render(request, 'view/comments.html',context)
class about (TemplateView):
    template_name = 'view/about.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        cart =Cart(self.request)
        context['CartNumber'] =len(cart)
        context['Cart'] =cart
        context['total'] =cart.get_total_price()
        return context

class privacy (TemplateView):
    template_name = 'view/privacy.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        cart =Cart(self.request)
        context['CartNumber'] =len(cart)
        context['Cart'] =cart
        context['total'] =cart.get_total_price()
        return context

class home_view (TemplateView):
    template_name = 'view/index.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        cart =Cart(self.request)
        context['CartNumber'] =len(cart)
        context['Cart'] =cart
        context['total'] =cart.get_total_price()
        context['off'] = list( product.objects.filter(status = True , Discoust__gt=25 )[:8])
        return context

class faq_view (TemplateView):
    template_name = 'view/faq.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        cart =Cart(self.request)
        context['CartNumber'] =len(cart)
        context['Cart'] =cart
        context['total'] =cart.get_total_price()
        return context


def custom_404_view(request, exception):
    return render(request, 'view/404.html', status=404)


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
