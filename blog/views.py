from django.shortcuts import render ,get_list_or_404
from home.models import product
# Create your views here.
def login_view (request):
    return render(request,'blog/enter.html')
def product_view(request,pid):
    # Product = product.objects.filter(status=True)
    p = get_list_or_404(product,pk=pid,status=True)
    context = {'products':p}
    return render(request, 'blog/pro.html',context)
def search_view (request):
    Product = product.objects.filter(status=True)
    if request.method == 'GET':
        Product = Product.filter(description__contains =request.GET.get('p'))
    context = {'products':Product}
    return render(request, 'view/prose.html',context)
